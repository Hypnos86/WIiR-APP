# Generated by Django 3.2.9 on 2022-01-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0012_auto_20220112_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='period',
            field=models.SmallIntegerField(null=True, verbose_name='Okres (mc)'),
        ),
    ]
