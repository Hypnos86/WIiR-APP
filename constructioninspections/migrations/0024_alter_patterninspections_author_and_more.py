# Generated by Django 4.1 on 2022-11-15 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fixedasset', '0007_alter_building_options'),
        ('constructioninspections', '0023_alter_patterninspections_conclusions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patterninspections',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='patterninspections',
            name='inspection_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructioninspections.typeinspection', verbose_name='Rodzaj przeglądu'),
        ),
        migrations.AlterField(
            model_name='patterninspections',
            name='no_inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixedasset.building', verbose_name='Obiekt'),
        ),
        migrations.AlterField(
            model_name='patterninspections',
            name='technical_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructioninspections.technicalcondition', verbose_name='Stan techniczny'),
        ),
    ]