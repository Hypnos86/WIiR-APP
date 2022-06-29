# Generated by Django 4.0.5 on 2022-06-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_accessmodule_contracts_immovables_module_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessmodule',
            name='contracts_immovables_module',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: Zespół Nieruchomości - Podgląd'),
        ),
        migrations.AlterField(
            model_name='accessmodule',
            name='contracts_immovables_module_edit',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: Zespół Nieruchomości - Edycja'),
        ),
        migrations.AlterField(
            model_name='accessmodule',
            name='listregister_exploatation_team_module',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: Zespół Eksploatacji - Podgląd'),
        ),
        migrations.AlterField(
            model_name='accessmodule',
            name='listregister_float_team_module',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: Zespół Mieszkaniowy - Podgląd'),
        ),
        migrations.AlterField(
            model_name='accessmodule',
            name='listregister_float_team_module_edit',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: Zespół Mieszkaniowy - Edycja'),
        ),
    ]
