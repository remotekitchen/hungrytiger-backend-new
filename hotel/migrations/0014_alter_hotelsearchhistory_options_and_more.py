# Generated by Django 4.2.19 on 2025-05-20 04:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hotel", "0013_alter_hotel_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hotelsearchhistory",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="savedhotel",
            options={"ordering": ["-created_at"]},
        ),
    ]
