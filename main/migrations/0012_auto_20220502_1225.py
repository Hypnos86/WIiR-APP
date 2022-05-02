# Generated by Django 3.2.9 on 2022-05-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_accessmodule_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessmodule',
            name='contracts_module',
        ),
        migrations.AddField(
            model_name='accessmodule',
            name='contracts_immovables_module',
            field=models.BooleanField(default=False, verbose_name='Moduł Umowy Najmu'),
        ),
        migrations.AddField(
            model_name='accessmodule',
            name='cpvdict_module',
            field=models.BooleanField(default=False, verbose_name='Moduł Rodzajowośc WIiR'),
        ),
    ]
