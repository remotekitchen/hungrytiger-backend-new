# Generated by Django 4.1.6 on 2024-01-01 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0058_alter_category_menu_alter_menuitem_menu_and_more'),
        ('reward', '0009_alter_additionalcondition_reward_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreward',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.location', verbose_name='Location'),
        ),
    ]
