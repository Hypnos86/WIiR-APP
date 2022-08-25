# Generated by Django 4.1 on 2022-08-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixedasset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='information',
            field=models.TextField(default='', null=True, verbose_name='Informacje'),
        ),
        migrations.AlterField(
            model_name='building',
            name='usable_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Powierzchnia użytkowa'),
        ),
        migrations.AlterField(
            model_name='building',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Kubatura'),
        ),
    ]
