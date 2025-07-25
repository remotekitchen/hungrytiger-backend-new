# Generated by Django 4.1.6 on 2023-05-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255, unique=True, verbose_name='Key')),
                ('value', models.TextField(verbose_name='Value')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
