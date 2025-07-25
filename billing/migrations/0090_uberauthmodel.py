# Generated by Django 4.1.6 on 2024-07-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0089_merge_20240614_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='UberAuthModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
