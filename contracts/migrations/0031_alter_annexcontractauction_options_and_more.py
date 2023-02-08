# Generated by Django 4.1 on 2023-02-08 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0030_alter_financialdocument_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annexcontractauction',
            options={'ordering': ['contract_auction', 'date'], 'verbose_name': 'Aneks na umowę ZZP', 'verbose_name_plural': 'U.10- Umowy ZZP - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='annexcontractmedia',
            options={'ordering': ['contract_media', 'date'], 'verbose_name': 'Aneks Umowy na media', 'verbose_name_plural': 'U.05- Umowy Media - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='anneximmovables',
            options={'ordering': ['contract_immovables', 'date_annex'], 'verbose_name': 'Aneks na umowę nieruchomości', 'verbose_name_plural': 'U.02 - Umowy Nieruchomości - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='contractauction',
            options={'ordering': ['date'], 'verbose_name': 'Umowa ZZP', 'verbose_name_plural': 'U.09 - Umowy ZZP'},
        ),
        migrations.AlterModelOptions(
            name='contractimmovables',
            options={'ordering': ['date'], 'verbose_name': 'Umowa nieruchomosci', 'verbose_name_plural': 'U.01 - Umowy Nieruchomości'},
        ),
        migrations.AlterModelOptions(
            name='contractmedia',
            options={'ordering': ['-date'], 'verbose_name': 'Umowa na Media', 'verbose_name_plural': 'U.04 - Umowy Media'},
        ),
        migrations.AlterModelOptions(
            name='financialdocument',
            options={'ordering': ['-date'], 'verbose_name': 'Dokument księgowy', 'verbose_name_plural': 'U.07 - Dokumenty księkowe'},
        ),
        migrations.AlterModelOptions(
            name='guarantee',
            options={'ordering': ['guarantee'], 'verbose_name': 'Gwarancja', 'verbose_name_plural': 'U.12 - Umowy ZZP - Rodzaje Gwarancji'},
        ),
        migrations.AlterModelOptions(
            name='guaranteesettlement',
            options={'ordering': ['deadline_settlement'], 'verbose_name': 'Rozliczenie umowy', 'verbose_name_plural': 'U.11 - Umowy ZZP - Rozliczenia umów: Gwarancje'},
        ),
        migrations.AlterModelOptions(
            name='legalbasic',
            options={'verbose_name': 'Podstawa prawna', 'verbose_name_plural': 'U.13 - Podstawy prawne'},
        ),
        migrations.AlterModelOptions(
            name='mediatype',
            options={'ordering': ['type'], 'verbose_name': 'Media', 'verbose_name_plural': 'U.06 - Umowy Media - Rodzaje Mediów'},
        ),
        migrations.AlterModelOptions(
            name='typeofcontract',
            options={'verbose_name': 'Rodzaj umowy', 'verbose_name_plural': 'U.03 - Umowy Nieruchomości - Rodzaje umów'},
        ),
        migrations.AlterModelOptions(
            name='unitmeasure',
            options={'ordering': ['id'], 'verbose_name': 'Jednostka miary', 'verbose_name_plural': 'U.08 - Jednostki miary'},
        ),
    ]