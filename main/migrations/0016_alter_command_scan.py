# Generated by Django 3.2.9 on 2022-05-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_commands_command'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='scan',
            field=models.FileField(upload_to='Commands/%Y-%m/', verbose_name='Skan polecenia'),
        ),
    ]