# Generated by Django 4.1.6 on 2023-12-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0005_rename_restaurant_whatsappcampaignhistory_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='is_memeber',
            field=models.BooleanField(default=False, verbose_name='is_member'),
        ),
    ]
