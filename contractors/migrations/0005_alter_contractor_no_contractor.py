# Generated by Django 3.2.9 on 2022-06-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0004_alter_contractor_no_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='no_contractor',
            field=models.IntegerField(unique=True, verbose_name='Nr. kontrahenta'),
        ),
    ]
