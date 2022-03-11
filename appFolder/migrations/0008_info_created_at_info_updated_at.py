# Generated by Django 4.0.1 on 2022-03-08 03:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appFolder', '0007_info_info_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 8, 3, 6, 47, 846493, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
