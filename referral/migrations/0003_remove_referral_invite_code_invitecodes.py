# Generated by Django 4.1.6 on 2024-07-30 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0002_staffreferral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referral',
            name='invite_code',
        ),
        migrations.CreateModel(
            name='InviteCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referral.referral', verbose_name='refer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
