# Generated by Django 4.0.5 on 2022-06-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_gllery_module_accessmodule_gallery_module_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessmodule',
            name='contracts_immovables_module',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: ZN - Podgląd'),
        ),
        migrations.AlterField(
            model_name='accessmodule',
            name='contracts_immovables_module_edit',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: ZN - Edycja'),
        ),
    ]