# Generated by Django 4.1.6 on 2023-10-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0047_alter_category_menu'),
        ('accounts', '0009_user_address'),
        ('marketing', '0002_voucher'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, verbose_name='Promotion name')),
                ('audience', models.CharField(choices=[('all', 'ALL'), ('members', 'MEMBERS')], default='all', max_length=20, verbose_name='Audience')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company', verbose_name='Company')),
                ('durations', models.ManyToManyField(blank=True, to='marketing.duration', verbose_name='Durations')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.location', verbose_name='Location')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Activation Campaign',
                'verbose_name_plural': 'Activation Campaigns',
            },
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='audience',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='company',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='durations',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='id',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='location',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='name',
        ),
        migrations.RemoveField(
            model_name='spendxsavey',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='audience',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='company',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='durations',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='id',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='location',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='voucher',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='spendxsavey',
            name='activationcampaign_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marketing.activationcampaign'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voucher',
            name='activationcampaign_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marketing.activationcampaign'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Bogo',
            fields=[
                ('activationcampaign_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marketing.activationcampaign')),
                ('items', models.ManyToManyField(blank=True, to='food.menuitem', verbose_name='Menu Items')),
            ],
            options={
                'verbose_name': 'Bogo',
                'verbose_name_plural': 'Bogo Campaigns',
            },
            bases=('marketing.activationcampaign',),
        ),
    ]
