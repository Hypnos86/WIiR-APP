# Generated by Django 3.2.9 on 2022-01-10 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0004_alter_powiat_swop_id'),
        ('contracts', '0006_alter_aneksimmovables_contractimmovables'),
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
                'verbose_name_plural': 'Umowy ZZP - Gwarancje',
            },
        ),
        migrations.CreateModel(
            name='LegalBasicZzp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_basic_zzp', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Podstawa prawna ZZP',
                'verbose_name_plural': 'Umowy ZZP - Tryb zamówień',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Okres',
                'verbose_name_plural': 'Okresy',
            },
        ),
        migrations.AlterModelOptions(
            name='anekscontractauction',
            options={'ordering': ['contract_auction', 'date'], 'verbose_name': 'Aneks ZZP', 'verbose_name_plural': 'Umowy ZZP (Aneksy)'},
        ),
        migrations.AlterModelOptions(
            name='aneksimmovables',
            options={'ordering': ['contractimmovables', 'data_aneksu'], 'verbose_name': 'Aneks', 'verbose_name_plural': 'Nieruchomosci - Aneksy do umów'},
        ),
        migrations.AlterModelOptions(
            name='contractauction',
            options={'ordering': ['date'], 'verbose_name': 'Umowa ZZP', 'verbose_name_plural': 'Umowy ZZP'},
        ),
        migrations.AlterModelOptions(
            name='contractimmovables',
            options={'ordering': ['data_umowy'], 'verbose_name': 'Umowa nieruchomosci', 'verbose_name_plural': 'Nieruchomości - Umowy'},
        ),
        migrations.AlterModelOptions(
            name='podstawa',
            options={'verbose_name': 'Podstawa prawna', 'verbose_name_plural': 'Nieruchomosci - Podstawy prawne'},
        ),
        migrations.AlterModelOptions(
            name='rodzaj',
            options={'verbose_name': 'Rodzaj umowy', 'verbose_name_plural': 'Nieruchomości - Rodzaje umów'},
        ),
        migrations.AlterModelOptions(
            name='stan',
            options={'verbose_name': 'Stan umowy', 'verbose_name_plural': 'Nieruchomości - Stany umów'},
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='contract_auction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='aneks_contract_auction', to='contracts.contractauction', verbose_name='Umowa ZZP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data utworzenia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='date',
            field=models.DateField(null=True, verbose_name='Data aneksu'),
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='price_after_change',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Kwota aneksu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='price_change',
            field=models.BooleanField(default=False, verbose_name='Zmiana wartości umowy'),
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='scan',
            field=models.FileField(blank=True, null=True, upload_to='contracts_zzp/annexes/%Y/', verbose_name='Skan aneksu'),
        ),
        migrations.AddField(
            model_name='anekscontractauction',
            name='scope_changes',
            field=models.TextField(blank=True, default='', verbose_name='Zakres zmian'),
        ),
        migrations.AddField(
            model_name='contractauction',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='auth.user', verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='change',
            field=models.DateTimeField(auto_now=True, verbose_name='Zmiana'),
        ),
        migrations.AddField(
            model_name='contractauction',
            name='contract_security',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Kwota zabezpiecznia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='contractor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contractors.contractor', verbose_name='Kontrahent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data utworzenia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data podpisania'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data zakończenia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='last_report_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data ostatniego protokołu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='no_contract',
            field=models.CharField(default=1, max_length=20, verbose_name='Nr. umowy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12, verbose_name='Wartość umowy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='scan',
            field=models.FileField(blank=True, null=True, upload_to='contracts_zzp_pdf/%Y/', verbose_name='Skan umowy'),
        ),
        migrations.AddField(
            model_name='contractauction',
            name='security_percentage',
            field=models.SmallIntegerField(default=1, verbose_name='Procent zabezpiecznia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='units.unit', verbose_name='Jednostka'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aneksimmovables',
            name='skan_aneksu',
            field=models.FileField(blank=True, null=True, upload_to='contracts_immovables/annexes/%Y/', verbose_name='Skan aneks'),
        ),
        migrations.AlterField(
            model_name='contractimmovables',
            name='podstawa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractimmovables', to='contracts.podstawa', verbose_name='Podstawa prawna'),
        ),
        migrations.CreateModel(
            name='GuaranteePeriod',
            fields=[
                ('period_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contracts.period')),
            ],
            bases=('contracts.period',),
        ),
        migrations.CreateModel(
            name='WarrantyPeriod',
            fields=[
                ('period_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contracts.period')),
            ],
            bases=('contracts.period',),
        ),
        migrations.AddField(
            model_name='contractauction',
            name='guarantee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.guarantee', verbose_name='Gwarancja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='legal_basic_zzp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.legalbasiczzp', verbose_name='Tryb UPZP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='guarantee_period',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.guaranteeperiod', verbose_name='Okres gwarancji'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractauction',
            name='warranty_period',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.warrantyperiod', verbose_name='Okres rękojmi'),
            preserve_default=False,
        ),
    ]