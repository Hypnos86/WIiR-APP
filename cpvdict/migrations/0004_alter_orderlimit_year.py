# Generated by Django 4.0.5 on 2022-07-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpvdict', '0003_remove_orderlimit_limit_brutto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlimit',
            name='year',
            field=models.IntegerField(unique=True, verbose_name='Rok'),
        ),
    ]