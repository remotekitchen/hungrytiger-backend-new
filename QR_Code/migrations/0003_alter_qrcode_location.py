# Generated by Django 4.1.6 on 2024-01-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0061_alter_menu_options_menu_showing'),
        ('QR_Code', '0002_qrcode_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food.location', verbose_name='location'),
        ),
    ]
