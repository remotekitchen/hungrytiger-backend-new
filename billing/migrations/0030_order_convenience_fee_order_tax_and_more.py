# Generated by Django 4.1.6 on 2023-10-12 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0047_alter_category_menu'),
        ('billing', '0029_alter_order_dropoff_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='convenience_fee',
            field=models.FloatField(default=0, verbose_name='Convenience Fee'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=0, verbose_name='Tax'),
        ),
        migrations.AlterField(
            model_name='deliveryfeeassociation',
            name='restaurant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='Restaurant'),
        ),
    ]
