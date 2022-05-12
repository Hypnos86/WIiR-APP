# Generated by Django 3.2.9 on 2022-05-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0003_remove_project_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_of_settlement',
            field=models.DateField(blank=True, null=True, verbose_name='Data rozliczenia'),
        ),
        migrations.AddField(
            model_name='project',
            name='settlement_scan',
            field=models.FileField(blank=True, null=True, upload_to='investments/settlements/%Y/', verbose_name='Rozliczenie inwestycyjne'),
        ),
        migrations.AlterField(
            model_name='project',
            name='investment_program',
            field=models.FileField(blank=True, null=True, upload_to='investments/investment_program/%Y/', verbose_name='Program inwestycji'),
        ),
    ]