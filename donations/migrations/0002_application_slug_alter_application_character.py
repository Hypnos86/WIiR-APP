# Generated by Django 4.1 on 2023-03-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='character',
            field=models.CharField(max_length=25, unique_for_year='date_receipt', verbose_name='Nr. sprawy'),
        ),
    ]
