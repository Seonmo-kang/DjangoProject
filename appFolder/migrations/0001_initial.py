# Generated by Django 4.0.1 on 2022-02-18 01:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.BigAutoField(primary_key=True, serialize=True, verbose_name='Hospital id')),
                ('hospital_name', models.CharField(max_length=150, verbose_name='Hospital name')),
                ('hospital_address1', models.CharField(max_length=200, verbose_name='Hospital address1')),
                ('hospital_address2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Hospital address2')),
                ('hospital_city', models.CharField(max_length=50, verbose_name='Hospital city')),
                ('hospital_state', models.CharField(max_length=40, verbose_name='Hospital state')),
                ('hospital_zipcode', models.CharField(default='10001', max_length=11, validators=[django.core.validators.RegexValidator('^([0-9]{5}(?:-[0-9]{4})?$)', 'Must be 00000 or 00000-0000', 'This is code')], verbose_name='Hospital zipcode')),
                ('hospital_x', models.FloatField(default=None, null=True, verbose_name='Hospital x')),
                ('hospital_y', models.FloatField(default=None, null=True, verbose_name='Hospital y')),
                ('hospital_vaccineType', models.CharField(choices=[('unknown', 'unknown'), ('pf', 'pfizer'), ('js', 'janssen'), ('all', 'all')], default='all', max_length=10, null=True, verbose_name='Hospital vaccineType')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('info_index', models.BigAutoField(primary_key=True, serialize=False, verbose_name='indexNum')),
                ('info_dateOfBirth', models.DateField(help_text='YYYY/MM/DD', verbose_name='date of birth')),
                ('info_zipCode', models.CharField(default='10001', max_length=11, validators=[django.core.validators.RegexValidator('^([0-9]{5}(?:-[0-9]{4})?$)', 'Must be 00000 or 00000-0000', 'This is code')], verbose_name='zipcode')),
                ('info_vaccine', models.CharField(choices=[('fd', 'First Dose'), ('bd', 'Booster Dose'), ('ad', 'Additional Dose')], max_length=2, verbose_name='vaccine')),
                ('info_vaccineType', models.CharField(choices=[('pf', 'pfizer'), ('js', 'janssen')], max_length=2, verbose_name='vaccine type')),
                ('info_consentAck', models.BooleanField(verbose_name='consent Ack')),
            ],
        ),
    ]
