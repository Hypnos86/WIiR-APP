# Generated by Django 4.1 on 2023-03-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='slug',
            field=models.SlugField(default='', max_length=80, null=True),
        ),
    ]