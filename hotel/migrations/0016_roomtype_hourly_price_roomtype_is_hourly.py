# Generated by Django 4.2.19 on 2025-05-26 03:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotel", "0015_roomtype_max_adults_roomtype_max_children"),
    ]

    operations = [
        migrations.AddField(
            model_name="roomtype",
            name="hourly_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=8, null=True
            ),
        ),
        migrations.AddField(
            model_name="roomtype",
            name="is_hourly",
            field=models.BooleanField(default=False),
        ),
    ]
