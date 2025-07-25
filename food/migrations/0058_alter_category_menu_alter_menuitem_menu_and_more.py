# Generated by Django 4.1.6 on 2023-11-14 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0057_alter_modifiergroup_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='modifiergroup',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='modifiergroup',
            name='used_by',
            field=models.ManyToManyField(to='food.menuitem', verbose_name='Used by'),
        ),
    ]
