# Generated by Django 4.2.19 on 2025-04-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_alter_user_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='Phone number'),
        ),
    ]
