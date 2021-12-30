# Generated by Django 3.2.9 on 2021-12-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpvdict', '0014_alter_order_cpv_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='type',
        ),
        migrations.AddField(
            model_name='order',
            name='typeorder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cpvdict.typeorder', verbose_name='Rodzaj zamówienia'),
            preserve_default=False,
        ),
    ]
