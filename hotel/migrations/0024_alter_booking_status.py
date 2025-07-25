# Generated by Django 4.2.19 on 2025-06-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotel", "0023_booking_idx_hotel_checkin_checkout_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("cancelled", "Cancelled"),
                    ("completed", "Completed"),
                    ("no_show", "No Show"),
                    ("checked_in", "Checked In"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
