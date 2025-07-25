# Generated by Django 4.1.6 on 2023-06-28 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0023_alter_menuitem_original_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='category',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Uid'),
        ),
        migrations.AddField(
            model_name='location',
            name='direct_order',
            field=models.BooleanField(default=False, verbose_name='Direct order'),
        ),
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='location',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Uid'),
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='menu',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Uid'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Uid'),
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Uid'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Uid'),
        ),
    ]
