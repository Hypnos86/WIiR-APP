# Generated by Django 4.0.5 on 2022-06-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_accessmodule_zok_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessmodule',
            name='commands',
            field=models.BooleanField(default=False, verbose_name='ZOPK - Polecenia'),
        ),
    ]
