# Generated by Django 4.1.6 on 2024-04-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_appstore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appstore',
            name='version',
            field=models.CharField(default='0.0.0', max_length=30, verbose_name='App Version'),
        ),
    ]
