# Generated by Django 4.0.5 on 2022-08-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0015_alter_unit_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='information',
            field=models.CharField(blank=True, max_length=200, verbose_name='Obiekt'),
        ),
    ]