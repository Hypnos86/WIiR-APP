# Generated by Django 3.2.9 on 2021-12-20 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpvdict', '0004_alter_orderingobject_name_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderingobject',
            name='leftSum',
        ),
        migrations.RemoveField(
            model_name='orderingobject',
            name='usedSum',
        ),
    ]