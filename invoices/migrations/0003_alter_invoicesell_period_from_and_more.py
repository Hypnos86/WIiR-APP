# Generated by Django 4.1 on 2023-09-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_invoicesell_period_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicesell',
            name='period_from',
            field=models.CharField(max_length=10, verbose_name='Okres od'),
        ),
        migrations.AlterField(
            model_name='invoicesell',
            name='period_to',
            field=models.CharField(max_length=10, verbose_name='Okres do'),
        ),
    ]
