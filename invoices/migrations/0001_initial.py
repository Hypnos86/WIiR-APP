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
        ('sourcefinancing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=20, verbose_name='Pracownik')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pracownik',
                'verbose_name_plural': 'Wystawcy faktur - sprzedaż',
            },
        ),
        migrations.CreateModel(
            name='Invoicesell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data wystawienia')),
                ('noinvoice', models.CharField(max_length=11, verbose_name='Nr. faktury')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kwota [zł]')),
                ('period_from', models.DateField(verbose_name='Okres od')),
                ('period_to', models.DateField(verbose_name='Okres do')),
                ('comments', models.TextField(blank=True, default='', verbose_name='Informacje')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicebuy', to=settings.AUTH_USER_MODEL)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicesell', to='contractors.contractor', verbose_name='Kontrahent')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicesell', to='invoices.creator', verbose_name='Osoba wystawiająca')),
                ('powiat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicesell', to='units.powiat', verbose_name='Powiat')),
            ],
            options={
                'verbose_name': 'Faktura sprzedaży',
                'verbose_name_plural': 'Faktury - sprzedaż',
            },
        ),
        migrations.CreateModel(
            name='Invoiceitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kwota [zł]')),
                ('acount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceitems', to='sourcefinancing.financesource', verbose_name='Konto')),
                ('powiat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceitems', to='units.powiat', verbose_name='Powiat')),
            ],
            options={
                'verbose_name': 'Element faktury',
                'verbose_name_plural': 'Elementy faktury',
            },
        ),
        migrations.CreateModel(
            name='Invoicebuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datawyplytu', models.DateField(verbose_name='Data wypływu')),
                ('data', models.DateField(verbose_name='Data wystawienia')),
                ('noinvoice', models.CharField(max_length=30, verbose_name='Nr. faktury')),
                ('period_from', models.DateField(verbose_name='Okres od')),
                ('period_to', models.DateField(verbose_name='Okres do')),
                ('comments', models.TextField(blank=True, default='', verbose_name='Informacje')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicesell', to=settings.AUTH_USER_MODEL)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicebuy', to='contractors.contractor', verbose_name='Kontrahent')),
                ('invoiceitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceitems', to='invoices.invoiceitems', verbose_name='Źródło finansowania')),
            ],
            options={
                'verbose_name': 'Faktura - kupno',
                'verbose_name_plural': 'Faktury - kupno',
            },
        ),
    ]
