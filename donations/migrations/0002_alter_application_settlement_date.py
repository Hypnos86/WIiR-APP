# Generated by Django 4.0.5 on 2022-07-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='settlement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data rozliczenia'),
        ),
    ]
