# Generated by Django 4.2.19 on 2025-03-19 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0083_alter_fissionprize_prize_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bxgy',
            name='free_items',
        ),
        migrations.RemoveField(
            model_name='bxgy',
            name='items',
        ),
    ]
