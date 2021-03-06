# Generated by Django 4.0.5 on 2022-07-22 07:29

import contracts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0006_alter_unit_city'),
        ('contractors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0002_contractmedia_mediatype'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmedia',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_media', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='change_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Zmiany'),
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='contractor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_media', to='contractors.contractor', verbose_name='Wykonawca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data utworzenia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='information',
            field=models.TextField(blank=True, default='', verbose_name='Informacje'),
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='no_contract',
            field=models.CharField(default=1, max_length=30, verbose_name='Nr.umowy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='scan',
            field=models.FileField(blank=True, null=True, upload_to=contracts.models.upload_contract_media, verbose_name='Skan'),
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Aktualna'),
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contractmedia', to='contracts.mediatype', verbose_name='Rodzaj umowy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractmedia',
            name='unit',
            field=models.ManyToManyField(related_name='contract_media', to='units.unit', verbose_name='Jednostka'),
        ),
        migrations.AlterField(
            model_name='annexcontractauction',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annexcontractauction', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
