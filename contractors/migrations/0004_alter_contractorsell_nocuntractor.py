# Generated by Django 3.2.9 on 2021-12-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0003_auto_20211208_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorsell',
            name='nocuntractor',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
