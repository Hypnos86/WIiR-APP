# Generated by Django 4.0.5 on 2022-07-21 19:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0003_alter_project_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='source_financing',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Źródło finansowania'),
        ),
    ]
