# Generated by Django 4.0.5 on 2022-07-11 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contractors', '0001_initial'),
        ('units', '0001_initial'),
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(max_length=4, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ogólna nazwa przedmiotu zamówienia w ujęciu rodzajowym')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Suma zamówień')),
                ('remain', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Pozostało')),
            ],
            options={
                'verbose_name': 'Przedmiot zamówienia',
                'verbose_name_plural': 'Klasyfikacja rodzajowa',
                'ordering': ['name_id'],
            },
        ),
        migrations.CreateModel(
            name='OrderLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Rok')),
                ('euro_exchange_rate', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Kurs euro')),
                ('limit_euro', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Limit euro')),
                ('limit_netto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Limit zamówień netto')),
                ('limit_brutto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Limit zamowień brutto')),
            ],
            options={
                'verbose_name': 'Limit zamówień',
                'verbose_name_plural': 'Limit zamówień',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat', models.SmallIntegerField(default=0, verbose_name='Podatek [%]')),
            ],
            options={
                'verbose_name': 'Podatek Vat',
                'verbose_name_plural': 'Rodzaje podatków vat',
            },
        ),
        migrations.CreateModel(
            name='Typecpv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_cpv', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'CPV',
                'verbose_name_plural': 'Słownik CPV',
            },
        ),
        migrations.CreateModel(
            name='TypeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, null=True, verbose_name='Rodzaj zamówienia')),
            ],
            options={
                'verbose_name': 'Rodzaj zamowienia',
                'verbose_name_plural': 'Rodzaj zamówienia',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('no_order', models.CharField(blank=True, default='', max_length=15, unique=True, verbose_name='Nr zlecenia')),
                ('sum_netto', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Kwota netto')),
                ('sum_brutto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kwota brutto')),
                ('brakedown', models.BooleanField(verbose_name='Awaria')),
                ('content', models.TextField(blank=True, default='', verbose_name='Zakres')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Data dodania')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='contractors.contractor', verbose_name='Kontrahent')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cpvdict.genre', verbose_name='ID rodzajowości')),
                ('typeorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cpvdict.typeorder', verbose_name='Rodzaj zamówienia')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='units.unit', verbose_name='Obiekt')),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cpvdict.tax', verbose_name='Podatek')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='main.employer', verbose_name='Branżysta')),
            ],
            options={
                'verbose_name': 'Zamówienie',
                'verbose_name_plural': 'Zamówienia',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='genre',
            name='cpv',
            field=models.ManyToManyField(related_name='Genre', to='cpvdict.typecpv', verbose_name='Kody CPV'),
        ),
    ]
