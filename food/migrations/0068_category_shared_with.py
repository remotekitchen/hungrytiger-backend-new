# Generated by Django 4.1.6 on 2024-04-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0067_menuitem_disabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shared_with',
            field=models.ManyToManyField(blank=True, null=True, related_name='shared_menu', to='food.menu', verbose_name='shared with'),
        ),
    ]
