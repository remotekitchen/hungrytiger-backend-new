# Generated by Django 4.2.19 on 2025-05-19 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0095_alter_activationcampaign_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='max_uses',
            field=models.PositiveIntegerField(default=1, help_text='Maximum number of times this voucher can be used.'),
        ),
    ]
