# Generated by Django 4.2.19 on 2025-05-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0164_rename_local_deals_order_local_deal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='local_deal',
        ),
        migrations.AddField(
            model_name='order',
            name='qr_code_value',
            field=models.CharField(blank=True, default=None, max_length=10, unique=True, verbose_name='QR Code Value'),
        ),
    ]
