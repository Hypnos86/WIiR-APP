# Generated by Django 3.2.9 on 2022-01-05 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_auto_20220105_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aneksimmovables',
            name='contractimmovables',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aneks', to='contracts.contractimmovables', verbose_name='Umowa'),
        ),
    ]