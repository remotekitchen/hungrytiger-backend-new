# Generated by Django 4.2.19 on 2025-05-06 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_rename_order_count_total_user_order_count_total_rk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='order_count_total_rk',
        ),
    ]
