# Generated by Django 4.0.5 on 2022-07-11 20:12

import contracts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contractors', '0001_initial'),
        ('main', '0001_initial'),
        ('units', '0001_initial'),
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guarantee', models.CharField(max_length=50, verbose_name='Gwarancja')),
            ],
            options={
                'verbose_name': 'Gwarancja',
                'verbose_name_plural': 'INW - Umowy - Gwarancja',
            },
        ),
        migrations.CreateModel(
            name='GuaranteePeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guarantee_period', models.SmallIntegerField(verbose_name='Okres gwarancji (mc)')),
            ],
            options={
                'verbose_name': 'Okres gwarancyjny',
                'verbose_name_plural': 'INW - Umowy - Okres gwarancyjne',
                'ordering': ['guarantee_period'],
            },
        ),
        migrations.CreateModel(
            name='LegalBasic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act', models.CharField(max_length=100, verbose_name='Ustawa')),
                ('legal_basic', models.CharField(max_length=30, verbose_name='Paragraf w ustawie')),
                ('legal_basic_text', models.TextField(verbose_name='Tekst paragrafu')),
            ],
            options={
                'verbose_name': 'Podstawa prawna',
                'verbose_name_plural': 'Podstawy prawne',
            },
        ),
        migrations.CreateModel(
            name='TypeOfContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Rodzaj umowy',
                'verbose_name_plural': 'Nieruchomo??ci - Rodzaje um??w',
            },
        ),
        migrations.CreateModel(
            name='WarrantyPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_period', models.SmallIntegerField(verbose_name='Okres r??kojmi (mc)')),
            ],
            options={
                'verbose_name': 'Okres r??kojmi',
                'verbose_name_plural': 'INW - Umowy - Okres r??kojmi',
                'ordering': ['warranty_period'],
            },
        ),
        migrations.CreateModel(
            name='ContractImmovables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('no_contract', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Nr umowy')),
                ('period_of_validity', models.DateField(blank=True, null=True, verbose_name='Okres obowi??zywania')),
                ('usable_area', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Powierzchnia u??ytkowa')),
                ('rent_cost', models.BooleanField(verbose_name='Czynsz')),
                ('electric_cost', models.BooleanField(verbose_name='Pr??d')),
                ('gas_cost', models.BooleanField(verbose_name='Gaz')),
                ('water_cost', models.BooleanField(verbose_name='Woda')),
                ('central_heating_cost', models.BooleanField(verbose_name='C.O.')),
                ('garbage_cost', models.BooleanField(verbose_name='??mieci')),
                ('garbage_tax_cost', models.BooleanField(verbose_name='Zagospodarowanie odpadami komunalnymi')),
                ('property_cost', models.BooleanField(verbose_name='Podatek od nieruchomo??ci')),
                ('scan', models.FileField(blank=True, null=True, upload_to=contracts.models.upload_scan_contract_immovables, verbose_name='Skan umowy')),
                ('state', models.BooleanField(default=True, verbose_name='Aktualna')),
                ('information', models.TextField(blank=True, default='', verbose_name='Informacje')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contractors.contractor', verbose_name='Kontrahent')),
                ('legal_basic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contracts.legalbasic', verbose_name='Podstawa prawna')),
                ('type_of_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contracts.typeofcontract', verbose_name='Rodzaj umowy')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='units.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name': 'Umowa nieruchomosci',
                'verbose_name_plural': 'Nieruchomo??ci - Umowy',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ContractAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('no_contract', models.CharField(max_length=20, unique=True, verbose_name='Nr. umowy')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Warto???? umowy')),
                ('work_scope', models.CharField(max_length=120, verbose_name='Przedmiot umowy')),
                ('end_date', models.DateField(verbose_name='Data zako??czenia')),
                ('last_report_date', models.DateField(blank=True, null=True, verbose_name='Data ostatniego protoko??u')),
                ('security_percent', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Procent zabezpiecznia')),
                ('security_sum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kwota zabezpiecznia')),
                ('report', models.TextField(blank=True, default='', verbose_name='Raportowanie')),
                ('information', models.TextField(blank=True, default='', verbose_name='Informacje')),
                ('scan', models.FileField(blank=True, null=True, upload_to=contracts.models.up_load_contract_auction, verbose_name='Skan umowy')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contractors.contractor', verbose_name='Kontrahent')),
                ('guarantee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.guarantee', verbose_name='Gwarancja')),
                ('guarantee_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.guaranteeperiod', verbose_name='Okres gwarancji')),
                ('investments_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='investments.project', verbose_name='Zadanie inwestycyjne')),
                ('legal_basic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.legalbasic', verbose_name='Tryb UPZP')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='units.unit', verbose_name='Jednostka')),
                ('warranty_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.warrantyperiod', verbose_name='Okres r??kojmi')),
                ('worker', models.ManyToManyField(related_name='contract_auction', to='main.employer', verbose_name='Inspektor')),
            ],
            options={
                'verbose_name': 'Umowa ZZP',
                'verbose_name_plural': 'INW - Umowy',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='AnnexImmovables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_annex', models.FileField(null=True, upload_to=contracts.models.upload_scan_annex_contract_immovables, verbose_name='Skan aneks')),
                ('date_annex', models.DateField(null=True, verbose_name='Data aneksu')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contract_immovables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annex', to='contracts.contractimmovables', verbose_name='umowa')),
            ],
            options={
                'verbose_name': 'Aneks',
                'verbose_name_plural': 'Nieruchomosci - Umowy - Aneksy',
                'ordering': ['contract_immovables', 'date_annex'],
            },
        ),
        migrations.CreateModel(
            name='AnnexContractAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data aneksu')),
                ('price_change', models.BooleanField(default=False, verbose_name='Zmiana warto??ci umowy')),
                ('price_after_change', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kwota aneksu')),
                ('scope_changes', models.TextField(blank=True, default='', verbose_name='Zakres zmian')),
                ('scan', models.FileField(blank=True, null=True, upload_to=contracts.models.up_load_annex_contract_auction, verbose_name='Skan aneksu')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contract_auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aneks_contract_auction', to='contracts.contractauction', verbose_name='Umowa ZZP')),
            ],
            options={
                'verbose_name': 'Aneks ZZP',
                'verbose_name_plural': 'INW - Umowy - Aneksy',
                'ordering': ['contract_auction', 'date'],
            },
        ),
    ]
