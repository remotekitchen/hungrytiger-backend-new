# Generated by Django 4.1.6 on 2024-11-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_otp_user_user_is_phone_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_phone_verified',
            field=models.BooleanField(default=False, verbose_name='is phone verified'),
        ),
    ]
