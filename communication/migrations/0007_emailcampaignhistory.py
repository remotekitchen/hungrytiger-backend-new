# Generated by Django 4.1.6 on 2023-12-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0058_alter_category_menu_alter_menuitem_menu_and_more'),
        ('communication', '0006_customerinfo_is_memeber'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCampaignHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('audience', models.CharField(blank=True, max_length=200, verbose_name='audience')),
                ('msg_from', models.CharField(blank=True, max_length=59, verbose_name='msg_from')),
                ('from_name', models.CharField(blank=True, max_length=59, verbose_name='from_name')),
                ('msg_to', models.CharField(blank=True, max_length=255, verbose_name='msg_to')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('textPart', models.CharField(blank=True, max_length=255, verbose_name='textPart')),
                ('htmlPart', models.CharField(blank=True, max_length=255, verbose_name='htmlPart')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='url')),
                ('time', models.DateTimeField(blank=True, verbose_name='time')),
                ('restaurant', models.ManyToManyField(blank=True, to='food.restaurant', verbose_name='restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
