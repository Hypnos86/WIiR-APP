# Generated by Django 3.2.9 on 2022-05-06 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0017_alter_contractimmovables_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
    ]
