# Generated by Django 4.0.5 on 2022-07-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpvdict', '0011_tax_remove_order_sum_order_sum_brutto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='vat',
            field=models.SmallIntegerField(default=0, verbose_name='Podatek [%]'),
        ),
    ]
