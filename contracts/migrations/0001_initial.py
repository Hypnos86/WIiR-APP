# Generated by Django 3.2.9 on 2021-12-03 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contractors', '0004_auto_20211203_1340'),
    ]

    operations = [
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
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_umowy', models.DateField(verbose_name='Data umowy')),
                ('nrumowy', models.CharField(blank=True, default='BRAK', max_length=20)),
                ('okres_obowiazywania', models.DateField(blank=True, null=True, verbose_name='Okres obowiązywania')),
                ('pow_uzyczona', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('koszt_prad', models.BooleanField()),
                ('inf_prad', models.TextField(blank=True, default='')),
                ('koszt_gaz', models.BooleanField()),
                ('inf_gaz', models.TextField(blank=True, default='')),
                ('koszt_woda', models.BooleanField()),
                ('inf_woda', models.TextField(blank=True, default='')),
                ('koszt_co', models.BooleanField()),
                ('inf_co', models.TextField(blank=True, default='')),
                ('skan', models.FileField(blank=True, null=True, upload_to='umowy_pdf')),
                ('comments', models.TextField(blank=True, default='', verbose_name='Uwagi')),
                ('archives', models.BooleanField(default=0)),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiana')),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kontrahent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.contractorsell')),
                ('podstawa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.podstawa')),
                ('rodzaj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.rodzaj')),
                ('stan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contracts.stan')),
            ],
        ),
    ]
