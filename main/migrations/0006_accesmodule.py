# Generated by Django 3.2.9 on 2022-04-19 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_employer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccesModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractors_module', models.BooleanField(default=0, verbose_name='Moduł Kontrahenci')),
                ('contracts_module', models.BooleanField(default=0, verbose_name='Moduł Umowy')),
                ('investments_module', models.BooleanField(default=0, verbose_name='Moduł Inwestycje')),
                ('invoices_module', models.BooleanField(default=0, verbose_name='Moduł Faktury')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accesmodule', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Dostęp do modułów',
                'verbose_name_plural': 'Dostęp do modułów',
            },
        ),
    ]