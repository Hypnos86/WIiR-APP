# Generated by Django 3.2.9 on 2022-05-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0012_alter_project_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_of_acceptance',
            field=models.DateField(blank=True, null=True, verbose_name='Data akceptacji programu'),
        ),
        migrations.AlterField(
            model_name='project',
            name='no_acceptance_document',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='L.dz. programu'),
        ),
    ]
