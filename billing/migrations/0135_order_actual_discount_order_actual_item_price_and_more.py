# Generated by Django 4.2.19 on 2025-04-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0134_restaurantcontract'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='actual_discount',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Actual Discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='actual_item_price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Actual Item Price'),
        ),
        migrations.AddField(
            model_name='order',
            name='amount_to_restaurant',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Amount to Restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='bogo_inflation_percentage',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='BOGO Inflation Percentage'),
        ),
        migrations.AddField(
            model_name='order',
            name='bogo_loss',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='BOGO Loss'),
        ),
        migrations.AddField(
            model_name='order',
            name='commission_amount',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Commission Amount'),
        ),
        migrations.AddField(
            model_name='order',
            name='hungry_tiger_discount',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Hungry Tiger Discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant_discount',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Restaurant Discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='selling_price_inclusive_tax',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Selling Price (Inclusive of Tax)'),
        ),
    ]
