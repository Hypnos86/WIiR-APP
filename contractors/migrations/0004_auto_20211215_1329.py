# Generated by Django 3.2.9 on 2021-12-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0003_rename_contractorsell_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='adres',
            field=models.CharField(max_length=30, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='informacje',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Informacje'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='kod_pocztowy',
            field=models.CharField(max_length=6, null=True, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='miasto',
            field=models.CharField(max_length=20, null=True, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='nazwa',
            field=models.CharField(max_length=30, null=True, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='nocuntractor',
            field=models.CharField(max_length=10, unique=True, verbose_name='Nr. kontrahenta'),
        ),
    ]