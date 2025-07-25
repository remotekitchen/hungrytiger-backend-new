# Generated by Django 4.1.6 on 2024-11-19 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0106_alter_restaurant_logo'),
        ('billing', '0116_unregisteredgiftcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='unregisteredgiftcard',
            name='restaurant',
            field=models.ForeignKey(default=83, on_delete=django.db.models.deletion.CASCADE, to='food.restaurant'),
            preserve_default=False,
        ),
    ]
