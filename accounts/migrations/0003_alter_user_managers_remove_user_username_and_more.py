# Generated by Django 4.1.6 on 2023-05-23 19:36

import accounts.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_company_credential'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
