# Generated by Django 3.2.9 on 2022-05-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0016_alter_contractimmovables_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractimmovables',
            name='state',
            field=models.BooleanField(default=True, verbose_name='aaa'),
        ),
    ]