# Generated by Django 3.2.9 on 2022-04-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_rename_inspector_contractauction_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalbasic',
            name='act',
            field=models.CharField(max_length=100, verbose_name='Ustawa'),
        ),
        migrations.AlterField(
            model_name='legalbasic',
            name='legal_basic',
            field=models.CharField(max_length=30, verbose_name='Paragraf w ustawie'),
        ),
        migrations.AlterField(
            model_name='legalbasic',
            name='legal_basic_text',
            field=models.TextField(verbose_name='Tekst paragrafu'),
        ),
    ]