# Generated by Django 4.1.6 on 2024-10-29 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0103_restaurant_accept_scheduled_order'),
        ('marketing', '0060_merge_20241008_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='activationcampaign',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.menu', verbose_name='Menu'),
        ),
    ]
