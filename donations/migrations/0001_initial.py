# Generated by Django 4.0.5 on 2022-07-11 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import donations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contractors', '0001_initial'),
        ('units', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=40, verbose_name='Rodzaj')),
            ],
            options={
                'verbose_name': 'Rodzaj darowizny',
                'verbose_name_plural': 'Rodzaje darowizn',
            },
        ),
        migrations.CreateModel(
            name='TypeFinancialResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=40, verbose_name='Rodzaj środków')),
            ],
            options={
                'verbose_name': 'Rodzaj środków',
                'verbose_name_plural': 'Rodzaje środków',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=25, verbose_name='Nr. sprawy')),
                ('date_receipt', models.DateField(verbose_name='Data wpływu')),
                ('date_return', models.DateField(verbose_name='Data zwrotu')),
                ('no_application', models.CharField(max_length=10, verbose_name='Nr. wniosku')),
                ('no_agreement', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nr. porozumienia')),
                ('date_agreement', models.DateField(verbose_name='Data porozumienia')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kwota darowizny')),
                ('settlement_date', models.DateField(verbose_name='Data rozliczenia')),
                ('subject', models.TextField(blank=True, null=True, verbose_name='Przedmiot porozumienia')),
                ('information', models.TextField(blank=True, default='', null=True, verbose_name='Informacje')),
                ('donation_scan', models.FileField(blank=True, null=True, upload_to=donations.models.upload_donation_scan, verbose_name='Skan porozumienia')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Data zmian')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('donation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='donations.typedonation', verbose_name='Rodzaj darowizny')),
                ('financial_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application', to='donations.typefinancialresources', verbose_name='Rodzaj środków')),
                ('presenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='contractors.contractor', verbose_name='Darczyńca')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='units.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name': 'Wniosek',
                'verbose_name_plural': 'Wnioski',
                'ordering': ['date_receipt'],
            },
        ),
    ]
