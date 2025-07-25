# Generated by Django 4.1.6 on 2024-03-27 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_merge_20240311_1241'),
        ('reward', '0017_userreward_expiry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rewardmanage',
            name='min_reward_point',
        ),
        migrations.RemoveField(
            model_name='rewardmanage',
            name='total_reward_point',
        ),
        migrations.RemoveField(
            model_name='rewardmanage',
            name='user',
        ),
        migrations.AddField(
            model_name='rewardmanage',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='rewardmanage',
            name='points_required',
            field=models.PositiveIntegerField(default=0, verbose_name='Points Required'),
        ),
    ]
