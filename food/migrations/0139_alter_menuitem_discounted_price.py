# Generated by Django 4.2.19 on 2025-05-27 03:39

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0138_merge_20250526_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), help_text='Base price after applying the restaurant discount', max_digits=10, null=True, verbose_name='Discounted Price'),
        ),
    ]
