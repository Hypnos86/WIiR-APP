# Generated by Django 3.2.9 on 2021-12-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator',
            options={'verbose_name': 'Wystawcy faktur', 'verbose_name_plural': 'Pracownik'},
        ),
    ]
