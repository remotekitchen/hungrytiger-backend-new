# Generated by Django 4.1.6 on 2025-02-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0120_restaurant_restaurant_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
    ]
