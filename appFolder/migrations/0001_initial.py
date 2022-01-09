# Generated by Django 4.0.1 on 2022-01-09 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('Hospital_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Hospital name')),
                ('Hospital_address1', models.CharField(max_length=20, verbose_name='Hospital address1')),
                ('Hospital_address2', models.CharField(blank=True, max_length=200, verbose_name='Hospital address2')),
                ('Hospital_city', models.CharField(max_length=20, verbose_name='Hospital city')),
                ('Hospital_state', models.CharField(max_length=10, verbose_name='Hospital state')),
                ('Hospital_zipcode', models.IntegerField(default=0, verbose_name='Hospital zipcode')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('info_index', models.BigAutoField(primary_key=True, serialize=False, verbose_name='indexNum')),
                ('info_dateOfBirth', models.DateField(help_text='DD/MM/YY', verbose_name='date of birth')),
                ('info_zipCode', models.IntegerField(verbose_name='zipcode')),
                ('info_vaccine', models.CharField(choices=[('fd', 'First Dose'), ('bd', 'Booster Dose'), ('ad', 'Additional Dose')], max_length=20, verbose_name='vaccine')),
                ('info_vaccineType', models.CharField(max_length=20, verbose_name='vaccine type')),
                ('info_consentAck', models.BooleanField(verbose_name='consent Ack')),
            ],
        ),
    ]
