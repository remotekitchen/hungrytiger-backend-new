# Generated by Django 4.1.6 on 2023-09-30 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0024_merge_0022_deliveryfeeassociation_0023_billingprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryfeeassociation',
            name='discount_in_percent',
            field=models.BooleanField(default=0, verbose_name='Give Discount'),
        ),
    ]
