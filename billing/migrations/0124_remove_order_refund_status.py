# Generated by Django 4.1.6 on 2024-12-17 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0123_order_refund_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='refund_status',
        ),
    ]
