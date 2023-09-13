# Generated by Django 4.1 on 2023-09-13 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50, verbose_name='Rodzaj')),
            ],
            options={
                'verbose_name': 'Rodzaj budynku',
                'verbose_name_plural': 'ST.02 - Rodzaje budynkuów',
                'ordering': ['kind'],
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_inventory', models.CharField(max_length=20, unique=True, verbose_name='Nr. inwentarzowy')),
                ('building_name', models.CharField(max_length=100, verbose_name='Nazwa obiektu')),
                ('usable_area', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Powierzchnia użytkowa')),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Kubatura')),
                ('information', models.TextField(blank=True, default='', null=True, verbose_name='Informacje')),
                ('state', models.BooleanField(default=True, verbose_name='Aktywny')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Data zmian')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to='fixedasset.kindbuilding', verbose_name='Rodzaj budynku')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to='units.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name': 'Budynek',
                'verbose_name_plural': 'ST.01 - Budynki',
                'ordering': ['unit'],
            },
        ),
    ]
