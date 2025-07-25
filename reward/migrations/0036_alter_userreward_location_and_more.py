# Generated by Django 4.2.19 on 2025-03-27 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0130_alter_restaurant_voucher_restriction'),
        ('reward', '0035_alter_userreward_audience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreward',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='userreward',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='Restaurant'),
        ),
    ]
