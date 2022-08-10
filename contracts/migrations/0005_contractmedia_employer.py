# Generated by Django 4.0.5 on 2022-07-22 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_accessmodule_units_accessmodule_units_edit'),
        ('contracts', '0004_alter_mediatype_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmedia',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_media', to='main.employer', verbose_name='Branżysta'),
            preserve_default=False,
        ),
    ]