# Generated by Django 4.1.6 on 2023-11-13 13:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0002_platform_logo_platformmenuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='client_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Client ID'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='client_secret',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Client secret'),
        ),
    ]
