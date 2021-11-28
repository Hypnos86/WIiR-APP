# Generated by Django 3.2.9 on 2021-11-27 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Powiat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powiat', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Jednostka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(max_length=30)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('miasto', models.CharField(max_length=20)),
                ('informacje', models.TextField(blank=True)),
                ('archiwum', models.BooleanField(default=0)),
                ('powiat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.powiat')),
                ('rodzaj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.rodzaj')),
            ],
        ),
    ]
