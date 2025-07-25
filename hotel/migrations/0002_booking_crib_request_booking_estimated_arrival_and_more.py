# Generated by Django 4.2.19 on 2025-05-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="crib_request",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="booking",
            name="estimated_arrival",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="extra_bed_request",
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name="hotel",
            index=models.Index(fields=["name"], name="hotel_hotel_name_7bbf9d_idx"),
        ),
        migrations.AddIndex(
            model_name="hotel",
            index=models.Index(
                fields=["is_active"], name="hotel_hotel_is_acti_940282_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="hotel",
            index=models.Index(
                fields=["star_rating"], name="hotel_hotel_star_ra_f62a6a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="roomavailability",
            index=models.Index(
                fields=["available_rooms"], name="hotel_rooma_availab_6e645c_idx"
            ),
        ),
    ]
