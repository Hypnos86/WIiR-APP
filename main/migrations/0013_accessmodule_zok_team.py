# Generated by Django 4.0.5 on 2022-06-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_accessmodule_contract_immovables_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessmodule',
            name='zok_team',
            field=models.BooleanField(default=False, verbose_name='Ewidencja: Zespoł Obsługi Kancelarynej'),
        ),
    ]
