# Generated by Django 4.1 on 2023-02-08 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operationalneedsrecords', '0012_alter_needsletter_isdone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metricscasetype',
            options={'ordering': ['metric_type'], 'verbose_name': 'Kategoria sprawy', 'verbose_name_plural': 'E.03 - Kategorie spraw'},
        ),
        migrations.AlterModelOptions(
            name='needsletter',
            options={'ordering': ['-receipt_date'], 'verbose_name': 'Ewidencja pism', 'verbose_name_plural': 'E.01 - Ewidencje Pism'},
        ),
        migrations.AlterModelOptions(
            name='registrationtype',
            options={'ordering': ['registration_type'], 'verbose_name': 'Rodzaj zgłoszenia', 'verbose_name_plural': 'E.02 - Rodzaje zgłoszeń'},
        ),
    ]