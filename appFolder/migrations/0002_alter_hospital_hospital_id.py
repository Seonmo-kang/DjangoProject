# Generated by Django 4.0.1 on 2022-02-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFolder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Hospital id'),
        ),
    ]
