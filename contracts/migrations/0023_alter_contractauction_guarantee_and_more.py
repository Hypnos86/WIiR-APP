# Generated by Django 4.1 on 2022-08-30 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0022_alter_guarantee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractauction',
            name='guarantee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_auction', to='contracts.guarantee', verbose_name='Gwarancja'),
        ),
        migrations.AlterField(
            model_name='contractauction',
            name='security_percent',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='Procent zabezpiecznia'),
        ),
    ]