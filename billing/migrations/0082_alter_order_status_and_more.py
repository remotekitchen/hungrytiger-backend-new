# Generated by Django 4.1.6 on 2024-05-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0081_order_uber_delivery_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('accepted', 'ACCEPTED'), ('scheduled_accepted', 'SCHEDULED_ACCEPTED'), ('not_ready_for_pickup', 'NOT_READY_FOR_PICKUP'), ('ready_for_pickup', 'READY_FOR_PICKUP'), ('rider_confirmed', 'RIDER_CONFIRMED'), ('rider_confirmed_pickup_arrival', 'RIDER_CONFIRMED_PICKUP_ARRIVAL'), ('rider_picked_up', 'RIDER_PICKED_UP'), ('rider_confirmed_dropoff_arrival', 'RIDER_CONFIRMED_DROPOFF_ARRIVAL'), ('completed', 'COMPLETED'), ('cancelled', 'CANCELLED'), ('rejected', 'REJECTED'), ('n/a', 'N/A')], default='pending', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_before_cancelled',
            field=models.CharField(blank=True, choices=[('pending', 'PENDING'), ('accepted', 'ACCEPTED'), ('scheduled_accepted', 'SCHEDULED_ACCEPTED'), ('not_ready_for_pickup', 'NOT_READY_FOR_PICKUP'), ('ready_for_pickup', 'READY_FOR_PICKUP'), ('rider_confirmed', 'RIDER_CONFIRMED'), ('rider_confirmed_pickup_arrival', 'RIDER_CONFIRMED_PICKUP_ARRIVAL'), ('rider_picked_up', 'RIDER_PICKED_UP'), ('rider_confirmed_dropoff_arrival', 'RIDER_CONFIRMED_DROPOFF_ARRIVAL'), ('completed', 'COMPLETED'), ('cancelled', 'CANCELLED'), ('rejected', 'REJECTED'), ('n/a', 'N/A')], default='n/a', max_length=50, verbose_name='Status before cancelled'),
        ),
    ]
