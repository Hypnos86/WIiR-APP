# Generated by Django 4.1 on 2022-11-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructioninspections', '0019_technicalcondition_component_use_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalcondition',
            name='component_use',
            field=models.CharField(max_length=9, verbose_name='Procent zużycia elementu'),
        ),
    ]