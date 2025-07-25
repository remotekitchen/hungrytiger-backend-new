# Generated by Django 4.1.6 on 2024-01-17 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0061_alter_menu_options_menu_showing'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('table_qrlink', models.CharField(blank=True, max_length=255, verbose_name='table_qr')),
                ('table_qrlink_scanned', models.IntegerField(verbose_name='table_qrlink_scanned')),
                ('banner_qrlink', models.CharField(blank=True, max_length=255, verbose_name='banner_qrlink')),
                ('banner_qrlink_scanned', models.IntegerField(verbose_name='table_qrlink_scanned')),
                ('social_qrlink', models.CharField(blank=True, max_length=255, verbose_name='social_qrlink')),
                ('social_qrlink_scanned', models.IntegerField(verbose_name='table_qrlink_scanned')),
                ('poster_qrlink', models.CharField(blank=True, max_length=255, verbose_name='poster_qrlink')),
                ('poster_qrlink_scanned', models.IntegerField(verbose_name='table_qrlink_scanned')),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
