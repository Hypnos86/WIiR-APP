# Generated by Django 3.2.9 on 2022-01-10 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=50, verbose_name='Uprawnienia')),
            ],
            options={
                'verbose_name': 'Typ uprawnień',
                'verbose_name_plural': 'Uprawnienia',
            },
        ),
        migrations.CreateModel(
            name='Inspector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=25, verbose_name='Nazwisko')),
                ('permissions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspector', to='main.permissionstype', verbose_name='Uprawnienia')),
            ],
            options={
                'verbose_name': 'Inspektor',
                'verbose_name_plural': 'Inspektorzy',
            },
        ),
    ]
