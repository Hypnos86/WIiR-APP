# Generated by Django 4.0.5 on 2022-06-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0010_alter_contractor_no_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='no_contractor',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Nr. kontrahenta'),
        ),
    ]