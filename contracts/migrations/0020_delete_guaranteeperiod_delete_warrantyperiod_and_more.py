# Generated by Django 4.1 on 2022-08-10 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0019_guaranteesettlement_delete_settlementcontractauction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GuaranteePeriod',
        ),
        migrations.DeleteModel(
            name='WarrantyPeriod',
        ),
        migrations.AlterModelOptions(
            name='guaranteesettlement',
            options={'ordering': ['dedline_settlement'], 'verbose_name': 'Rozliczenie umowy', 'verbose_name_plural': 'Umowy ZZP - Rozliczenia umów: Gwarancje'},
        ),
    ]