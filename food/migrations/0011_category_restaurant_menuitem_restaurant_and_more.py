# Generated by Django 4.1.6 on 2023-05-26 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_alter_location_hours_alter_restaurant_opening_hours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='Restaurant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='Restaurant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to='food.restaurant', verbose_name='Restaurant'),
            preserve_default=False,
        ),
    ]
