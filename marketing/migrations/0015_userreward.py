# Generated by Django 4.1.6 on 2023-11-23 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0058_alter_category_menu_alter_menuitem_menu_and_more'),
        ('marketing', '0014_alter_fissioncampaign_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, max_length=150, verbose_name='Code')),
                ('reward_type', models.CharField(blank=True, max_length=150, verbose_name='Reward Type')),
                ('amount', models.FloatField(default=0, verbose_name='Amount')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.location', verbose_name='Restaurant')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Reward',
                'verbose_name_plural': 'User Rewards',
            },
        ),
    ]
