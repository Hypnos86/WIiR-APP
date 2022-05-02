# Generated by Django 3.2.9 on 2022-05-02 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_auto_20220419_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractors_module', models.BooleanField(default=False, verbose_name='Moduł Kontrahenci')),
                ('contracts_module', models.BooleanField(default=False, verbose_name='Moduł Umowy')),
                ('investments_module', models.BooleanField(default=False, verbose_name='Moduł Inwestycje')),
                ('invoices_module', models.BooleanField(default=False, verbose_name='Moduł Faktury')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessmodule', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Dostęp do modułów',
                'verbose_name_plural': 'Dostęp do modułów',
            },
        ),
        migrations.DeleteModel(
            name='AccesModule',
        ),
    ]
