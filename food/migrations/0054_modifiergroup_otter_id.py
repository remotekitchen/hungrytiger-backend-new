# Generated by Django 4.1.6 on 2023-11-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0053_alter_timetable_opening_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifiergroup',
            name='otter_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='otter identifier'),
        ),
    ]
