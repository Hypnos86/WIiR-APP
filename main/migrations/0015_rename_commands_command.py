# Generated by Django 3.2.9 on 2022-05-06 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_commands'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commands',
            new_name='Command',
        ),
    ]