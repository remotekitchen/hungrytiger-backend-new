# Generated by Django 4.1.6 on 2024-01-30 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0061_alter_menu_options_menu_showing'),
        ('billing', '0058_transactions_restaurant_wallet_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.location', verbose_name='Location'),
        ),
    ]
