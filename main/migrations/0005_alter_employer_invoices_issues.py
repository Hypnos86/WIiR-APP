# Generated by Django 4.0.5 on 2022-07-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_employer_invoices_issues_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='invoices_issues',
            field=models.BooleanField(default=0, verbose_name='Wystawianie faktur'),
        ),
    ]