# Generated by Django 3.2.9 on 2022-05-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listregister', '0004_auto_20220506_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialflat',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Wolne'),
        ),
    ]
