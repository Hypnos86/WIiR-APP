# Generated by Django 3.2.9 on 2022-05-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0006_project_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='realized',
            field=models.BooleanField(default=False, verbose_name='Zrealizowane'),
        ),
    ]