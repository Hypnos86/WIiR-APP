# Generated by Django 3.2.9 on 2022-04-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220419_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesmodule',
            name='contractors_module',
            field=models.BooleanField(default=0, verbose_name='Moduł Kontrahenci'),
        ),
        migrations.AlterField(
            model_name='accesmodule',
            name='investments_module',
            field=models.BooleanField(default=0, verbose_name='Moduł Inwestycje'),
        ),
    ]
