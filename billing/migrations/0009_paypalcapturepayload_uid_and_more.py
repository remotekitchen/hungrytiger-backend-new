# Generated by Django 4.1.6 on 2023-08-02 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0008_paypalcapturepayload'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypalcapturepayload',
            name='uid',
            field=models.CharField(blank=True, max_length=250, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='paypalcapturepayload',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paypal_payloads', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('purchase_token', models.TextField(verbose_name='Purchase Token')),
                ('purchase_time', models.DateTimeField(verbose_name='Purchase Time')),
                ('purchase_type', models.CharField(blank=True, choices=[('sandbox', 'SANDBOX'), ('production', 'PRODUCTION')], default='production', max_length=30, null=True, verbose_name='Purchase Type')),
                ('region', models.CharField(blank=True, max_length=50, verbose_name='Region Code')),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.order', verbose_name='Order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.AddField(
            model_name='paypalcapturepayload',
            name='purchase',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.purchase', verbose_name='Purchase'),
        ),
    ]
