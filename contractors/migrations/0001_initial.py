# Generated by Django 4.1 on 2023-09-13 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_contractor', models.IntegerField(blank=True, default='', null=True, unique=True, verbose_name='Nr. kontrahenta')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nazwa')),
                ('nip', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='NIP')),
                ('address', models.CharField(max_length=30, null=True, verbose_name='Adres')),
                ('zip_code', models.CharField(max_length=6, null=True, verbose_name='Kod pocztowy')),
                ('city', models.CharField(max_length=20, null=True, verbose_name='Miasto')),
                ('information', models.TextField(blank=True, default='', null=True, verbose_name='Informacje')),
                ('slug', models.SlugField(unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Zmiany')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Kontrahenci',
                'verbose_name_plural': 'K.01 - Kontrahenci',
                'ordering': ['name'],
                'unique_together': {('no_contractor', 'nip')},
            },
        ),
    ]
