import json
import pytz
from django.utils import timezone
from datetime import datetime, timedelta
from threading import Thread, Timer
from django.utils.timezone import now
from marketing.utils.send_sms import send_sms_bd

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from chatchef.settings import ENV_TYPE
from billing.models import Order
from billing.utilities.send_order_status_notification import (
    send_new_order_notification_to_restaurant_helper,
    send_order_sms_notification, send_order_status_notification_to_user)
from core.utils import get_logger

from .utiils import check_for_order_status_and_call
from billing.clients.raider_app import Raider_Client
from firebase.utils.fcm_helper import  get_dynamic_message, send_push_notification
from firebase.models import TokenFCM
from food.models import Restaurant
from django.core.exceptions import ObjectDoesNotExist
from billing.utiils import send_order_receipt
import threading
import time
from billing.tasks import check_order_acceptance
from django.db.models import Q
from billing.clients.doordash_client import DoordashClient
from django.db import transaction
from billing.utilities.order_rewards import OrderRewards

logger = get_logger()


@receiver(post_save, sender=Order)
def manage_order_rewards(sender, instance: Order, created, **kwargs):
      if not created:
          return

      # Schedule the task 2 hours after either scheduled_time or receive_date
      time = instance.scheduled_time if instance.scheduled_time else instance.receive_date + timedelta(hours=2)

      # Ensure the time is in the future to avoid immediate execution
      if time <= now():
          time = now() + timedelta(minutes=1)

      scheduled_obj = ClockedSchedule.objects.create(clocked_time=time)
      PeriodicTask.objects.create(
          name=f"order checker set for {time} --> {instance.id}",
          task="chatchef.order_checker",
          kwargs=json.dumps({'pk': instance.id}),
          clocked=scheduled_obj,
          one_off=True,
      )


@receiver(pre_save, sender=Order)
def send_order_status_notification(sender, instance: Order, **kwargs):
    try:
        send_notification = False
        if instance.id is not None:
            order = Order.objects.get(id=instance.id)

            if order.status != instance.status or (
                    order.is_paid != instance.is_paid and instance.is_paid is True and instance.payment_method !=
                    Order.PaymentMethod.CASH):
                send_notification = True

        elif instance.payment_method == Order.PaymentMethod.CASH:
            send_notification = True

        if send_notification:
            # Send fcm notification
            thread = Thread(
                target=send_order_status_notification_to_user, args=(instance,)
            )
            thread.start()
            # Send sms
            sms_thread = Thread(
                target=send_order_sms_notification, args=(instance,)
            )
            sms_thread.start()
    except:
        pass


@receiver(pre_save, sender=Order)
def send_new_order_notification_to_restaurant(sender, instance: Order, **kwargs):
    print("Signal triggered: New order saved")
    logger.info(f"Order data before save: {instance}")
    try:
        send_notification = False

        if not instance.id:
            # ✅ This is a brand new order being created
            if (
                instance.status in ["cancelled", "completed", "rejected"]
                or (instance.payment_method == Order.PaymentMethod.STRIPE and not instance.is_paid)
            ):
                print(
                    f"Skipping notification for new Order (status={instance.status}, is_paid={instance.is_paid})"
                )
                return
            else:
                send_notification = True
        else:
            order = Order.objects.get(id=instance.id)

            # ✅ Notify if payment was just completed (non-cash)
            if (
                instance.payment_method != Order.PaymentMethod.CASH
                and order.is_paid != instance.is_paid
                and instance.is_paid is True
            ):
                send_notification = True
                print("inner me --- 400", send_notification)

                # ✅ Mark reward coupon as claimed if any
                if instance.reward_coupon is not None:
                    user_reward = instance.reward_coupon
                    user_reward.is_claimed = True
                    user_reward.save(update_fields=["is_claimed"])

            # ✅ Notify if scheduled order just got accepted
            if (
                instance.status == Order.StatusChoices.SCHEDULED_ACCEPTED
                and instance.scheduling_type == Order.SchedulingType.FIXED_TIME
            ):
                send_notification = True

        print("before thread ----- 300", send_notification)
        if send_notification:
            thread = Thread(
                target=send_new_order_notification_to_restaurant_helper,
                args=(instance,),
            )
            thread.start()

            # call restaurant if order is pending
            timer = Timer(120, check_for_order_status_and_call, args=(instance.id,))
            timer.start()

    except Exception as e:
        logger.error(
            f"Send new notification signal error order id -> {instance.id} :: {e}"
        )

# Cache to track the order status before saving
PREVIOUS_ORDER_STATUSES = {}
ORDER_EXISTENCE={}

@receiver(pre_save, sender=Order)
def cache_previous_status(sender, instance, **kwargs):
    """
    Cache the previous status of the order so we can compare it in post_save.
    """
    if instance.pk is None:
        # New order, no previous status
        PREVIOUS_ORDER_STATUSES[instance.pk] = None
        return

    try:
        old_instance = sender.objects.get(pk=instance.pk)
        PREVIOUS_ORDER_STATUSES[instance.pk] = old_instance.status
        print(f"[PRE_SAVE] Existing order found: ID {instance.pk}, status = {old_instance.status}")
    except sender.DoesNotExist:
        PREVIOUS_ORDER_STATUSES[instance.pk] = None
        print(f"[PRE_SAVE] Order with ID {instance.pk} not found in DB")

    try:
        old_instance = sender.objects.get(pk=instance.pk)
        PREVIOUS_ORDER_STATUSES[instance.pk] = old_instance.status
        ORDER_EXISTENCE[instance.pk] = True
        print(f"[PRE_SAVE] Existing order found: ID {instance.pk}, status = {old_instance.status}")
    except sender.DoesNotExist:
        PREVIOUS_ORDER_STATUSES[instance.pk] = None
        ORDER_EXISTENCE[instance.pk] = False
        print(f"[PRE_SAVE] Order with ID {instance.pk} not found in DB")

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    truly_created = getattr(instance, 'is_new', False)
    print(f"[POST_SAVE] is_new flag passed: {truly_created}")

    user = instance.user
    tokens = list(TokenFCM.objects.filter(user=user).values_list("token", flat=True))

    if not tokens:
        return

    if truly_created:
        # New order — always send notification
        event_type = instance.status
    else:
        # Status change? Check previous status
        previous_status = PREVIOUS_ORDER_STATUSES.get(instance.pk)

        if previous_status == instance.status:
            print("[POST_SAVE] Status unchanged, skipping notification.")
            return

        event_type = instance.status
        print("[POST_SAVE] Status changed, sending notification.")

    restaurant_name = instance.restaurant.name if instance.restaurant else "Unknown Restaurant"
    title, body = get_dynamic_message(instance, event_type, restaurant_name)

    print("[POST_SAVE] Sending notification:", title, body)

    data = {
        "campaign_title": title,
        "campaign_message": body,
        "restaurant_name": restaurant_name,
        "screen": "restaurant",
        "id": 70  
    }


    send_push_notification(tokens, data)

    # Clean up the cache
    if instance.pk in PREVIOUS_ORDER_STATUSES:
        del PREVIOUS_ORDER_STATUSES[instance.pk]
        print("[POST_SAVE] Cleaned up cached status.")


# def delayed_send(order_id):
#     time.sleep(2)  # wait for is_paid to be updated
    
#     order = Order.objects.get(pk=order_id)
#     print(order.is_paid, order.restaurant, order.restaurant.is_remote_Kitchen, order.restaurant.is_chatchef_bd, 'order------------>')
#     if order.is_paid and order.restaurant and not order.restaurant.is_remote_Kitchen:
#         send_order_receipt(order_id=order_id)

# @receiver(post_save, sender=Order)
# def send_receipt_on_order_created(sender, instance, created, **kwargs):
#     if created:
#         print("top one")
#         if not instance.restaurant.is_remote_Kitchen:
#             print(f"Order {instance.order_id} created. Sending receipt...")
#             send_order_receipt(order_id=instance.pk)
#         elif instance.restaurant.is_remote_Kitchen:
#             print(f"Order {instance.order_id} created For hungry. Sending receipt...")
#             send_order_receipt(order_id=instance.pk)
#         else:
#             print(f"Order {instance.order_id} created. No receipt sent as restaurant is not remote kitchen.")
        
        
@receiver(post_save, sender=Order)
def send_receipt_on_order_created(sender, instance, created, **kwargs):
    if created:
        print("🕒 Delaying receipt for 1 second...")

        def delayed_receipt():
            if not instance.restaurant.is_remote_Kitchen:
                print(f"Order {instance.order_id} created. Sending receipt...")
            else:
                print(f"Order {instance.order_id} created For hungry. Sending receipt...")

            send_order_receipt(order_id=instance.pk)

        # Delay by 1 second to allow OrderItems to save
        threading.Timer(1.0, delayed_receipt).start()

   


_previous_status_cache = {}

@receiver(pre_save, sender=Order)
def cache_previous_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            prev = Order.objects.get(pk=instance.pk)
            _previous_status_cache[instance.pk] = prev.status
        except Order.DoesNotExist:
            pass


@receiver(post_save, sender=Order)
def trigger_receipt_on_status_change(sender, instance, **kwargs):
    previous_status = _previous_status_cache.pop(instance.pk, None)
    if previous_status and previous_status != instance.status:
        if instance.restaurant and (instance.is_paid or instance.restaurant.is_remote_Kitchen):
            print(f"Status changed for order {instance.order_id}. Sending receipt...")
            send_order_receipt(order_id=instance.pk)

            
@receiver(pre_save, sender=Order)
def trigger_receipt_on_status_change(sender, instance, **kwargs):
    print("done one")
    if not instance.pk:
        return  

    try:
        previous = Order.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        return

    # Check if status has changed
    if previous.status != instance.status:
        # Check required conditions
        print(instance.restaurant, instance.restaurant.is_remote_Kitchen, 'instances------------>')
        if instance.restaurant and (instance.is_paid or instance.restaurant.is_remote_Kitchen):
            print(f"Status changed for order {instance.order_id}. Sending receipt...")
            send_order_receipt(order_id=instance.pk)



@receiver(post_save, sender=Order)
def order_placed(sender, instance, created, **kwargs):
    """
    Signal handler that triggers when a new order is created.
    Schedules the first check for order acceptance after 60 seconds.
    """
    if created:
        logger.info(f"New order created (ID: {instance.id}). Scheduling acceptance check.")
        # Trigger Celery task to check order acceptance after 60 seconds
        check_order_acceptance.apply_async(args=[instance.id], countdown=60)


@receiver(post_save, sender=Order)
def handle_local_deal_redeem(sender, instance, created, **kwargs):
    """
    Handle local deal redemption automatically when the status is updated to 'COMPLETED'.
    This will set redeemed_at to current Bangladesh Time (BDT).
    """
    # Check if it's a local deal and the order status is COMPLETED
    if instance.status == Order.StatusChoices.COMPLETED and instance.order_method == Order.OrderMethod.LOCAL_DEAL:
        # Prevent recursion if redemption has already been done
        if not instance.is_local_deal_redeemed:
            # Set is_local_deal_redeemed to True
            instance.is_local_deal_redeemed = True
            
            # Convert current time (UTC) to Bangladesh Time (BDT)
            bdt_timezone = pytz.timezone('Asia/Dhaka')  # BDT (UTC +6)
            utc_time = timezone.now()  # This is UTC time by default
            
            # Convert UTC time to BDT
            bdt_time = utc_time.astimezone(bdt_timezone)  # Convert to Bangladesh Time (BDT)

            # Set redeemed_at to the current Bangladesh Time (BDT)
            instance.redeemed_at = bdt_time
            instance.is_paid = True  # Set the order as paid

            # Set delivery_time to redeemed_at (since this could be the time of redemption)
            instance.delivery_time = bdt_time

            # Save the changes with update_fields to avoid recursion
            instance.save(update_fields=["is_local_deal_redeemed", "redeemed_at", "is_paid", "delivery_time"])

@receiver(post_save, sender=Order)
def set_restaurant_accepted_time(sender, instance, created, **kwargs):
    """
    Set restaurant_accepted_time when order status is set to 'accepted'.
    """
    if instance.status == Order.StatusChoices.ACCEPTED and not instance.restaurant_accepted_time:
        logger.info(f"Order {instance.id} marked as 'accepted'. Saving restaurant_accepted_time.")
        bdt = pytz.timezone('Asia/Dhaka')
        bdt_time = timezone.now().astimezone(bdt)
        instance.restaurant_accepted_time = bdt_time
        instance.save(update_fields=["restaurant_accepted_time"])



_order_old_status_cache = {}

@receiver(pre_save, sender=Order)
def cache_old_order_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            old = Order.objects.get(pk=instance.pk)
            _order_old_status_cache[instance.pk] = old.status
        except Order.DoesNotExist:
            _order_old_status_cache[instance.pk] = None

@receiver(post_save, sender=Order)
def update_user_order_count(sender, instance, **kwargs):
    user = instance.user
    if not user:
        return

    # Only proceed if the order is paid or cash
    if instance.payment_method != Order.PaymentMethod.CASH and not instance.is_paid:
        return

    old_status = _order_old_status_cache.pop(instance.pk, None)
    new_status = instance.status

    # Update only if status changed to or from 'completed'
    if old_status != new_status and ('completed' in [old_status, new_status]):
        count = Order.objects.filter(
            user=user,
            status=Order.StatusChoices.COMPLETED
        ).filter(
            Q(payment_method=Order.PaymentMethod.CASH) | Q(is_paid=True)
        ).count()

        user.order_count_total_rk = count
        user.save(update_fields=["order_count_total_rk"])
        print(f"✅ Updated order count for user {user.id}: {count}")



@receiver(pre_save, sender=Order)
def auto_accept_vegan_order(sender, instance, **kwargs):
    if not instance._state.adding:
        return  # Skip for existing orders being updated

    if instance.restaurant and instance.restaurant.auto_accept_orders:
        if instance.status == Order.StatusChoices.PENDING:
            if instance.scheduled_time:
                instance.status = Order.StatusChoices.SCHEDULED_ACCEPTED
            else:
                instance.status = Order.StatusChoices.ACCEPTED

            # Handle pickup and delivery time
            prep_time = getattr(instance, "prep_time", 30)

            if instance.status == Order.StatusChoices.SCHEDULED_ACCEPTED:
                instance.delivery_time = instance.scheduled_time
            else:
                instance.pickup_time = timezone.now() + timedelta(minutes=prep_time)

            # Rewards for CASH payment
            if instance.payment_method == Order.PaymentMethod.CASH:
                OrderRewards().main(order=instance)

            # NOTE: Do not create delivery here – defer to post_save with transaction.on_commit()


@receiver(post_save, sender=Order)
def create_delivery_if_vegan(sender, instance, created, **kwargs):
    if instance.restaurant and instance.restaurant.auto_accept_orders:
        if instance.status in (Order.StatusChoices.ACCEPTED, Order.StatusChoices.SCHEDULED_ACCEPTED):
            if instance.order_method in (Order.OrderMethod.DELIVERY, Order.OrderMethod.RESTAURANT_DELIVERY):
                transaction.on_commit(lambda: safe_create_delivery(instance))


def safe_create_delivery(instance):
    try:
        if not instance.restaurant_id:
            print(f"Missing restaurant ID for Order {instance.id}")
            return

        doordash = DoordashClient()
        doordash.create_delivery(instance=instance)

    except Exception as e:
        print(f"Delivery creation failed for Order {instance.id}: {e}")

# @receiver(post_save, sender=Order)
# def send_sms_on_order_created(sender, instance, created, **kwargs):
#     if not created:
#         return

#     def _send_sms():
#         if ENV_TYPE != "DEVELOPMENT":
#             print("SMS not sent (non-production)")
#             return

#         if not instance.restaurant.is_remote_Kitchen:
#             print("Restaurant is not remote kitchen, SMS not sent.")
#             return

#         # Mapping of phone numbers to (name, greeting)
#         sms_recipients = {
#             # "01711690821": {"name": "Amena", "greeting": "Hey Sweet"},
#             "01980796731": {"name": "Sohag", "greeting": "Dear"},
#             # "01334923595": {"name": "Chion", "greeting": "Hi"},
#         }

#         order_mode = instance.get_order_method_display().upper()
#         order_type_label = (
#             "🛍️ Pickup Order"
#             if instance.order_method == Order.OrderMethod.PICKUP
#             else "🚚 Delivery Order"
#         )
#         order_time = (
#             instance.receive_date_ht.strftime("%Y-%m-%d %H:%M")
#             if instance.receive_date_ht
#             else "N/A"
#         )
#         voucher_code = instance.solid_voucher_code or "None"
#         payment_method = instance.get_payment_method_display().upper()
#         platform = (
#             instance.get_delivery_platform_display()
#             if instance.delivery_platform
#             else "N/A"
#         )

#         # Get ordered items from related model
#         ordered_items = instance.orderitem_set.all()

#         if not ordered_items:
#             items_text = "❌ No items found."
#         else:
#             items_text = ""
#             for i, item in enumerate(ordered_items, start=1):
#                 item_name = item.menu_item.name if item.menu_item else "Item"
#                 qty = item.quantity
#                 discount = (
#                     f"{item.discount_amount} off"
#                     if getattr(item, "discount_amount", 0)
#                     else "No discount"
#                 )
#                 items_text += f"\n{i}. {item_name} x{qty} ({discount})"

#         for phone, info in sms_recipients.items():
#             name = info["name"]
#             greeting = info["greeting"]

#             text = (
#                 f"{order_type_label} 🌟\n\n"
#                 f"{greeting} {name}! 🌈✨\n\n"
#                 f"🔥 A fresh order has landed in your kingdom!\n\n"
#                 f"🏪 *Restaurant:* {instance.restaurant.name}\n"
#                 f"🆔 *Order ID:* {instance.order_id}\n"
#                 f"🕒 *Time:* {order_time}\n"
#                 f"🛒 *Mode:* {order_mode}\n"
#                 f"💳 *Payment:* {payment_method}\n"
#                 f"🎟️ *Voucher:* {voucher_code}\n"
#                 f"🛵 *Platform:* {platform}\n\n"
#                 f"👤 *Customer:* {instance.customer}\n"
#                 f"📞 *Phone:* {instance.dropoff_phone_number}\n"
#                 f"📍 *Address:* {instance.dropoff_address}\n\n"
#                 f"📝 *Items:*{items_text}\n\n"
#                 f"💰 *Total:* {instance.total} {instance.currency.upper()}\n\n"
#                 f"🙏 You’re simply the best.\n"
#                 f"💪 Keep rocking it!"
#             )

#             try:
#                 res = send_sms_bd(phone, text)
#                 response = res.json()
#                 print(f"SMS sent to {phone}: {response}")
#             except Exception as e:
#                 print(f"SMS failed for {phone}: {e}")

#     transaction.on_commit(_send_sms)