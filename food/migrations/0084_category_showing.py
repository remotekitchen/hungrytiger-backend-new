# Generated by Django 4.1.6 on 2024-05-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0083_restaurant_stripe_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='showing',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
