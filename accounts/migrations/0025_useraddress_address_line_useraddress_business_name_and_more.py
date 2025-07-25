# Generated by Django 4.1.6 on 2024-05-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_company_register_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='address_line',
            field=models.CharField(blank=True, max_length=255, verbose_name='Address Line'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='business_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='Business Name'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='delivery_instructions',
            field=models.TextField(blank=True, max_length=500, verbose_name='Delivery Instructions'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='label',
            field=models.CharField(blank=True, max_length=50, verbose_name='Label'),
        ),
    ]
