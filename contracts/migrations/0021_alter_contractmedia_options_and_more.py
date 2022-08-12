# Generated by Django 4.1 on 2022-08-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0020_delete_guaranteeperiod_delete_warrantyperiod_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractmedia',
            options={'ordering': ['-date'], 'verbose_name': 'Umowa na Media', 'verbose_name_plural': 'Umowy Media'},
        ),
        migrations.AlterField(
            model_name='guaranteesettlement',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GuaranteeSettlement', to='contracts.contractauction', verbose_name='Umowa'),
        ),
    ]