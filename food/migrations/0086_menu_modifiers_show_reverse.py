# Generated by Django 4.1.6 on 2024-06-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0085_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='modifiers_show_reverse',
            field=models.BooleanField(default=False, verbose_name='modifiers show reverse'),
        ),
    ]
