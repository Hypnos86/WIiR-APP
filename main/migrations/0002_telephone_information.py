# Generated by Django 3.2.9 on 2021-12-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telephone',
            name='information',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Informacje'),
        ),
    ]