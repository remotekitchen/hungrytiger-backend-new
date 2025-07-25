# Generated by Django 4.1.6 on 2023-09-28 22:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_address'),
        ('billing', '0022_stripeconnectaccount_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('payout_account_id', models.TextField(blank=True, verbose_name='Payout Account ID')),
                ('last_payout_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last Payout Date')),
                ('payout_frequency', models.IntegerField(blank=True, choices=[(1, 'DAILY'), (7, 'WEEKLY')], default=7, verbose_name='Payout Frequency')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.company', verbose_name='Company')),
                ('stripe_connect_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.stripeconnectaccount', verbose_name='Stripe Connect Account')),
            ],
            options={
                'verbose_name': 'Billing Profile',
                'verbose_name_plural': 'Billing Profiles',
            },
        ),
    ]
