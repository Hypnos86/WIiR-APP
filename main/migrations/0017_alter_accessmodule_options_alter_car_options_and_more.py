# Generated by Django 4.1 on 2023-02-08 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_car_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessmodule',
            options={'verbose_name': 'Dostęp do modułów', 'verbose_name_plural': 'S.01 - Dostęp do modułów'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-rent_date'], 'verbose_name': 'Samochód sużbowy', 'verbose_name_plural': 'S.08 - Samochód służbowy'},
        ),
        migrations.AlterModelOptions(
            name='command',
            options={'ordering': ['create_date'], 'verbose_name': 'Polecenie', 'verbose_name_plural': 'S.07 - Polecenia'},
        ),
        migrations.AlterModelOptions(
            name='employer',
            options={'ordering': ['team', 'last_name'], 'verbose_name': 'Pracownik', 'verbose_name_plural': 'S.04 - Pracownicy'},
        ),
        migrations.AlterModelOptions(
            name='industrytype',
            options={'verbose_name': 'Branża', 'verbose_name_plural': 'S.03 - Branże'},
        ),
        migrations.AlterModelOptions(
            name='organisationtelephone',
            options={'verbose_name': 'Książka telefoniczna KWP w Poznaniu', 'verbose_name_plural': 'S.06 - Książka telefoniczna KWP w Poznaniu'},
        ),
        migrations.AlterModelOptions(
            name='secretariattelephone',
            options={'verbose_name': 'Telefon do sekretariatu', 'verbose_name_plural': 'S.05 - Telefony do sekretariatu'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['priority'], 'verbose_name': 'Komórka Wydziału', 'verbose_name_plural': 'S.02 - Komórki Wydziału'},
        ),
    ]
