# Generated by Django 4.0.5 on 2022-07-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_accessmodule_units_accessmodule_units_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessmodule',
            name='contract_media',
            field=models.BooleanField(default=False, verbose_name='ZE - Umowy Media - Podgląd'),
        ),
        migrations.AddField(
            model_name='accessmodule',
            name='contract_media_edit',
            field=models.BooleanField(default=False, verbose_name='ZE - Umowy Media - Edycja'),
        ),
    ]
