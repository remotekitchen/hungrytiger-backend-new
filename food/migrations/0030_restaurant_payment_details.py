# Generated by Django 4.1.6 on 2023-08-08 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_paymentdetails'),
        ('food', '0029_menuitem_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='payment_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.paymentdetails', verbose_name='Payment Details'),
        ),
    ]
