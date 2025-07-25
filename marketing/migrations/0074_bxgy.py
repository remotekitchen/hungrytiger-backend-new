# Generated by Django 4.2.19 on 2025-03-15 07:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0128_merge_20250211_0424'),
        ('marketing', '0073_alter_voucher_available_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='BxGy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_disabled', models.BooleanField(default=False, help_text='Disable this campaign without deleting it.')),
                ('buy', models.PositiveIntegerField(default=1, help_text='Number of items required to buy.', validators=[django.core.validators.MinValueValidator(1)])),
                ('get', models.PositiveIntegerField(default=1, help_text='Number of items given as a reward.', validators=[django.core.validators.MinValueValidator(1)])),
                ('discount_percent', models.PositiveIntegerField(default=100, help_text="Discount percentage applied to the 'get' item(s). 100% means free.", validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('applies_to_different_items', models.BooleanField(default=True, help_text="If True, 'get' items can be different from 'buy' items.")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('free_items', models.ManyToManyField(blank=True, help_text='Items that can be given for free if different from the bought items.', related_name='bxgy_free_items', to='food.menuitem', verbose_name='Free Items')),
                ('items', models.ManyToManyField(blank=True, help_text='Items that customers need to buy to qualify for the offer.', related_name='bxgy_campaigns', to='food.menuitem', verbose_name='Menu Items')),
            ],
            options={
                'verbose_name': 'Buy X Get Y Campaign',
                'verbose_name_plural': 'Buy X Get Y Campaigns',
            },
        ),
    ]
