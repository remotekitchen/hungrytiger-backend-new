# Generated by Django 4.1.6 on 2024-03-25 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0066_restaurant_reward_point_equivalent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(max_length=150)),
                ('secondary_color', models.CharField(max_length=150)),
                ('positive_color', models.CharField(max_length=150)),
                ('danger_color', models.CharField(max_length=150)),
                ('warning_color', models.CharField(max_length=150)),
                ('cart_color', models.CharField(max_length=150)),
                ('background_color', models.CharField(max_length=150)),
                ('text_color', models.CharField(max_length=150)),
                ('stock_color', models.CharField(max_length=150)),
                ('disable_color', models.CharField(max_length=150)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_theme', to='food.location', verbose_name='location')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_theme', to='food.restaurant', verbose_name='Restaurant')),
            ],
        ),
    ]
