# Generated by Django 4.0.5 on 2022-08-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0010_alter_unit_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Miasto'),
        ),
    ]