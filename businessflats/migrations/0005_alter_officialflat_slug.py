# Generated by Django 4.1 on 2023-03-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessflats', '0004_alter_officialflat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialflat',
            name='slug',
            field=models.SlugField(default='', null=True, unique=True),
        ),
    ]
