# Generated by Django 4.1.6 on 2024-11-25 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0108_menuitem_allow_group_order'),
        ('remotekitchen', '0002_grouporder'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouporder',
            name='is_taking_order',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='GroupOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(blank=True, to='food.menuitem', verbose_name='items')),
                ('restaurant', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.restaurant', verbose_name='Restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
