# Generated by Django 4.1.6 on 2023-05-23 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_company_credential'),
        ('food', '0004_alter_order_receive_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company', verbose_name='Company'),
        ),
    ]
