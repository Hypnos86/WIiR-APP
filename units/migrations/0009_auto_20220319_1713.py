# Generated by Django 3.2.9 on 2022-03-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0008_alter_unit_unit_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='informacje',
            field=models.TextField(blank=True, verbose_name='Informacje'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='kod_pocztowy',
            field=models.CharField(max_length=6, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='miasto',
            field=models.CharField(max_length=20, verbose_name='miasto'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='owner',
            field=models.CharField(max_length=50, verbose_name='Właściciel'),
        ),
    ]
