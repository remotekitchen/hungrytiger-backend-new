# Generated by Django 4.2.19 on 2025-05-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0172_merge_20250526_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receive_date_ht',
            field=models.DateTimeField(blank=True, help_text='Additional receive date for HT (HungryTiger) or specific purpose', null=True, verbose_name='Receive Date (HT)'),
        ),
    ]
