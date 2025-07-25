# Generated by Django 4.1.6 on 2024-01-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0047_alter_order_bogo_alter_order_purchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_method',
            field=models.CharField(choices=[('delivery', 'DELIVERY'), ('restaurant_delivery', 'RESTAURANT_DELIVERY'), ('pickup', 'PICKUP'), ('dine_in', 'DINE_IN')], default='delivery', max_length=20, verbose_name='Order method'),
        ),
    ]
