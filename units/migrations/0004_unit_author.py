# Generated by Django 4.0.5 on 2022-07-20 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0003_unit_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Autor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
