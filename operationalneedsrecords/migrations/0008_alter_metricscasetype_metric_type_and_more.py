# Generated by Django 4.1 on 2023-01-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationalneedsrecords', '0007_alter_metricscasetype_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricscasetype',
            name='metric_type',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='registrationtype',
            name='registration_type',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
