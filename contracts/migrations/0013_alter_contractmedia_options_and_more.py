# Generated by Django 4.0.5 on 2022-08-03 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0012_alter_annexcontractmedia_scan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractmedia',
            options={'verbose_name': 'Umowa na Media', 'verbose_name_plural': 'Umowy Media'},
        ),
        migrations.AlterField(
            model_name='annexcontractmedia',
            name='contract_media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annexcontractmedia', to='contracts.contractmedia', verbose_name='Umowa'),
        ),
    ]
