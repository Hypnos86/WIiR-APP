# Generated by Django 4.0.5 on 2022-07-11 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialFlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Adres')),
                ('area', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Powierzchnia')),
                ('room_numbers', models.IntegerField(blank=True, null=True, verbose_name='Ilość pomieszczeń')),
                ('flor', models.IntegerField(blank=True, null=True, verbose_name='Piętro')),
                ('state', models.BooleanField(default=True, verbose_name='Wolne')),
                ('information', models.TextField(blank=True, null=True, verbose_name='Informacje')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('change', models.DateTimeField(auto_now=True, verbose_name='Data zmian')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officialflat', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Mieszkanie służbowe',
                'verbose_name_plural': 'Mieszkania służbowe',
            },
        ),
    ]
