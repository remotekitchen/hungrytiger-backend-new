# Generated by Django 4.1.6 on 2024-08-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0097_menuitem_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.CharField(default='0.0', max_length=20),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.CharField(default='0.0', max_length=20),
        ),
    ]
