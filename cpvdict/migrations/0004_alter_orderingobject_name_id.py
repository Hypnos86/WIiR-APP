# Generated by Django 3.2.9 on 2021-12-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpvdict', '0003_alter_orderingobject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderingobject',
            name='name_id',
            field=models.CharField(max_length=4, unique=True, verbose_name='ID'),
        ),
    ]
