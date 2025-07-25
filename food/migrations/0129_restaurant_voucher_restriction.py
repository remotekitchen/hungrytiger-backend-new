# Generated by Django 4.2.19 on 2025-03-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0128_merge_20250211_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='voucher_restriction',
            field=models.BooleanField(default=False, help_text='Restrict the use of vouchers with other vouchers to this restaurant.', verbose_name='Voucher Restriction'),
        ),
    ]
