# Generated by Django 3.2.9 on 2022-01-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_rename_security_percentage_contractauction_security_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractauction',
            name='informations',
            field=models.TextField(blank=True, default='', verbose_name='Informacje'),
        ),
        migrations.AddField(
            model_name='contractauction',
            name='raports',
            field=models.TextField(blank=True, default='', verbose_name='Raportowanie'),
        ),
    ]
