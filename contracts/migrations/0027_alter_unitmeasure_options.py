# Generated by Django 4.1 on 2023-02-05 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0026_unitmeasure_financialdocument'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unitmeasure',
            options={'ordering': ['id'], 'verbose_name': 'Jednostka miary', 'verbose_name_plural': 'jednostki miary'},
        ),
    ]