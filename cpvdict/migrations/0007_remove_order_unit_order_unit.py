# Generated by Django 4.0.5 on 2022-08-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0006_alter_unit_city'),
        ('cpvdict', '0006_alter_orderlimit_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='unit',
        ),
        migrations.AddField(
            model_name='order',
            name='unit',
            field=models.ManyToManyField(related_name='order', to='units.unit', verbose_name='Obiekt'),
        ),
    ]