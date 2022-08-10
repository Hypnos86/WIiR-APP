# Generated by Django 4.0.5 on 2022-08-03 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0013_alter_contractmedia_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annexcontractauction',
            options={'ordering': ['contract_auction', 'date'], 'verbose_name': 'Aneks na umowę ZZP', 'verbose_name_plural': 'Umowy ZZP - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='anneximmovables',
            options={'ordering': ['contract_immovables', 'date_annex'], 'verbose_name': 'Aneks na umowę nieruchomości', 'verbose_name_plural': 'Umowy Nieruchomości - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='contractauction',
            options={'ordering': ['date'], 'verbose_name': 'Umowa ZZP', 'verbose_name_plural': 'Umowy ZZP'},
        ),
        migrations.AlterModelOptions(
            name='contractimmovables',
            options={'ordering': ['date'], 'verbose_name': 'Umowa nieruchomosci', 'verbose_name_plural': 'Umowy Nieruchomości'},
        ),
        migrations.AlterModelOptions(
            name='guarantee',
            options={'verbose_name': 'Gwarancja', 'verbose_name_plural': 'Umowy ZZP - Rodzaje Gwarancji'},
        ),
        migrations.AlterModelOptions(
            name='guaranteeperiod',
            options={'ordering': ['guarantee_period'], 'verbose_name': 'Okres gwarancyjny', 'verbose_name_plural': 'Umowy ZZP - Okres gwarancyjny'},
        ),
        migrations.AlterModelOptions(
            name='mediatype',
            options={'ordering': ['type'], 'verbose_name': 'Media', 'verbose_name_plural': 'Umowy Media - Rodzaje Mediów'},
        ),
        migrations.AlterModelOptions(
            name='settlementcontractauction',
            options={'ordering': ['first_part_security_date', 'second_part_security_date'], 'verbose_name': 'Rozliczenie umowy', 'verbose_name_plural': 'Umowy ZZP - Rozliczenia umów'},
        ),
        migrations.AlterModelOptions(
            name='typeofcontract',
            options={'verbose_name': 'Rodzaj umowy', 'verbose_name_plural': 'Umowy Nieruchomości - Rodzaje umów'},
        ),
        migrations.AlterModelOptions(
            name='warrantyperiod',
            options={'ordering': ['warranty_period'], 'verbose_name': 'Okres rękojmi', 'verbose_name_plural': 'Umowy ZZP - Okres rękojmi'},
        ),
    ]