# Generated by Django 3.2.9 on 2022-05-06 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0013_auto_20220505_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annexcontractauction',
            options={'ordering': ['contract_auction', 'date'], 'verbose_name': 'Aneks ZZP', 'verbose_name_plural': 'INW - Umowy - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='anneximmovables',
            options={'ordering': ['contract_immovables', 'date_annex'], 'verbose_name': 'Aneks', 'verbose_name_plural': 'Nieruchomosci - Umowy - Aneksy'},
        ),
        migrations.AlterModelOptions(
            name='contractauction',
            options={'ordering': ['date'], 'verbose_name': 'Umowa ZZP', 'verbose_name_plural': 'INW - Umowy'},
        ),
        migrations.AlterModelOptions(
            name='guarantee',
            options={'verbose_name': 'Gwarancja', 'verbose_name_plural': 'INW - Umowy - Gwarancja'},
        ),
        migrations.AlterModelOptions(
            name='guaranteeperiod',
            options={'ordering': ['guarantee_period'], 'verbose_name': 'Okres gwarancyjny', 'verbose_name_plural': 'INW - Umowy - Okres gwarancyjne'},
        ),
        migrations.AlterModelOptions(
            name='warrantyperiod',
            options={'ordering': ['warranty_period'], 'verbose_name': 'Okres rękojmi', 'verbose_name_plural': 'INW - Umowy - Okres rękojmi'},
        ),
    ]