# Generated by Django 4.2.19 on 2025-05-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0039_localdeal_deal_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='localdeal',
            name='main_price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Base price of the menu item', max_digits=10),
        ),
    ]
