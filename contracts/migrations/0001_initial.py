# Generated by Django 3.2.9 on 2022-01-03 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contractors', '0001_initial'),
        ('units', '0004_alter_powiat_swop_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AneksContractAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ContractAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Podstawa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podstawa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Podstawa prawna',
                'verbose_name_plural': 'Podstawy prawne',
            },
        ),
        migrations.CreateModel(
            name='Rodzaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Rodzaj umowy',
                'verbose_name_plural': 'Rodzaje umów',
            },
        ),
        migrations.CreateModel(
            name='Stan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stan', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Stan umowy',
                'verbose_name_plural': 'Stany umów',
            },
        ),
        migrations.CreateModel(
            name='ContractImmovables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_umowy', models.DateField(verbose_name='Data umowy')),
                ('nrumowy', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Nr umowy')),
                ('okres_obowiazywania', models.DateField(blank=True, null=True, verbose_name='Okres obowiązywania')),
                ('pow_uzyczona', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Powierzchnia użytkowa')),
                ('koszt_czynsz', models.BooleanField(verbose_name='Czynsz')),
                ('koszt_prad', models.BooleanField(verbose_name='Prąd')),
                ('koszt_gaz', models.BooleanField(verbose_name='Gaz')),
                ('koszt_woda', models.BooleanField(verbose_name='Woda')),
                ('koszt_co', models.BooleanField(verbose_name='C.O.')),
                ('koszt_smieci', models.BooleanField(verbose_name='Śmieci')),
                ('koszt_podsmiec', models.BooleanField(verbose_name='Zagospodarowanie odpadami komunalnymi')),
                ('koszt_podnier', models.BooleanField(verbose_name='Podatek od nieruchomości')),
                ('skan', models.FileField(blank=True, null=True, upload_to='contracts_immovables_pdf/%Y/', verbose_name='Skan umowy')),
                ('comments', models.TextField(blank=True, default='', verbose_name='Informacje')),
                ('archives', models.BooleanField(default=1, verbose_name='Aktywna')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kontrahent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contractors.contractor', verbose_name='Kontrahent')),
                ('podstawa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contracts.podstawa', verbose_name='Podstawa prawna')),
                ('rodzaj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contracts.rodzaj', verbose_name='Rodzaj umowy')),
                ('stan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contracts.stan')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='units.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name': 'Umowa nieruchomosci',
                'verbose_name_plural': 'Umowy nieruchomosci',
            },
        ),
        migrations.CreateModel(
            name='AneksImmovables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skan_aneksu', models.FileField(blank=True, null=True, upload_to='contracts_immovables_pdf/aneksy_pdf/%Y/', verbose_name='Skan aneks')),
                ('data_aneksu', models.DateField(null=True, verbose_name='Data aneksu')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aneks', to='contracts.contractimmovables', verbose_name='Umowa')),
            ],
            options={
                'verbose_name': 'Aneks',
                'verbose_name_plural': 'Aneksy',
            },
        ),
    ]
