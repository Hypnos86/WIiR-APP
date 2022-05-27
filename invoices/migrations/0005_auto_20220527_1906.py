# Generated by Django 3.2.9 on 2022-05-27 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20220527_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoicebuy',
            options={'ordering': ['date_receipt'], 'verbose_name': 'Faktura - kupno', 'verbose_name_plural': 'Faktury - kupno'},
        ),
        migrations.AlterModelOptions(
            name='invoicesell',
            options={'ordering': ['date'], 'verbose_name': 'Faktura sprzedaży', 'verbose_name_plural': 'Faktury - sprzedaż'},
        ),
        migrations.RemoveField(
            model_name='invoicebuy',
            name='invoice_items',
        ),
        migrations.AddField(
            model_name='invoiceitems',
            name='invoice_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invoiceitems', to='invoices.invoicebuy', verbose_name='ID Faktury'),
            preserve_default=False,
        ),
    ]
