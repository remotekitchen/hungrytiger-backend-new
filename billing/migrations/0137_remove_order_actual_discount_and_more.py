# Generated by Django 4.2.19 on 2025-04-13 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0136_order_ht_delivery_fee_expense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='actual_discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='actual_item_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount_to_restaurant',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bogo_inflation_percentage',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bogo_loss',
        ),
        migrations.RemoveField(
            model_name='order',
            name='commission_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='hungry_tiger_discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurant_discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='selling_price_inclusive_tax',
        ),
    ]
