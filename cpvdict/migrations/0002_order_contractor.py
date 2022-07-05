# Generated by Django 4.0.5 on 2022-06-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0006_alter_contractor_nip'),
        ('cpvdict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contractor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='contractors.contractor', verbose_name='Kontrahent'),
            preserve_default=False,
        ),
    ]