# Generated by Django 4.0.5 on 2022-08-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0012_alter_unit_address_alter_unit_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='manager',
            field=models.CharField(default='Policja', max_length=150, verbose_name='Trwały zarząd'),
        ),
    ]
