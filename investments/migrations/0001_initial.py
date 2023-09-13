# Generated by Django 4.1 on 2023-09-13 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import investments.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
        ('sourcefinancing', '0001_initial'),
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_acceptance', models.DateField(blank=True, null=True, verbose_name='Data programu')),
                ('no_acceptance_document', models.CharField(blank=True, max_length=15, null=True, verbose_name='L.dz. programu')),
                ('investment_program', models.FileField(blank=True, null=True, upload_to=investments.models.upload_scan, verbose_name='Program inwestycji')),
                ('project_title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Pełna nazwa zadania')),
                ('investment_cost_estimate_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='WKI')),
                ('source_financing', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Źródło finansowania')),
                ('information', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Informacje')),
                ('date_of_settlement', models.DateField(blank=True, null=True, verbose_name='Data rozliczenia')),
                ('settlement_scan', models.FileField(blank=True, null=True, upload_to=investments.models.upload_scan, verbose_name='Rozliczenie inwestycyjne')),
                ('realized', models.BooleanField(default=False, verbose_name='Zrealizowane')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='sourcefinancing.group', verbose_name='Grupa')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='sourcefinancing.paragraph', verbose_name='Paragraf')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='sourcefinancing.section', verbose_name='Rozdział')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='units.unit', verbose_name='Jednostka')),
                ('worker', models.ManyToManyField(related_name='project', to='main.employer', verbose_name='Inspektor')),
            ],
            options={
                'verbose_name': 'Zadanie inwestycyjne',
                'verbose_name_plural': 'I.01 - Zadania inwestycyjne',
                'ordering': ['date_of_acceptance'],
            },
        ),
    ]
