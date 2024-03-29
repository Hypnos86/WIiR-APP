# Generated by Django 4.1 on 2023-09-13 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetricsCaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_type', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Kategoria sprawy',
                'verbose_name_plural': 'E.03 - Kategorie spraw',
                'ordering': ['metric_type'],
            },
        ),
        migrations.CreateModel(
            name='RegistrationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_type', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Rodzaj zgłoszenia',
                'verbose_name_plural': 'E.02 - Rodzaje zgłoszeń',
                'ordering': ['registration_type'],
            },
        ),
        migrations.CreateModel(
            name='NeedsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateField(null=True, verbose_name='Data wpływu')),
                ('case_sign', models.CharField(max_length=50, null=True, verbose_name='Znak pisma')),
                ('case_description', models.TextField(verbose_name='Opis sprawy')),
                ('no_secretariats_diary', models.PositiveIntegerField(unique_for_year='receipt_date', verbose_name='Nr. z dziennika')),
                ('receipt_date_to_team', models.DateField(blank=True, verbose_name='Data wpływu do Zespołu')),
                ('case_sign_team', models.CharField(blank=True, max_length=30, null=True, verbose_name='Znak sprawy WiiR')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Koszt realizacji')),
                ('execution_date', models.DateField(blank=True, null=True, verbose_name='Data realizacji')),
                ('isDone', models.BooleanField(default=False, verbose_name='Zrealizowane')),
                ('information', models.TextField(blank=True, verbose_name='Informacje')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needsletter', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('case_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needsletter', to='operationalneedsrecords.metricscasetype', verbose_name='Rodzaj sprawy')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needsletter', to='main.employer', verbose_name='Branżysta')),
                ('registration_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needsletter', to='operationalneedsrecords.registrationtype', verbose_name='Rodzaj zgłoszenia')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needsletter', to='units.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name': 'Ewidencja pism',
                'verbose_name_plural': 'E.01 - Ewidencje Pism',
                'ordering': ['-receipt_date'],
            },
        ),
    ]
