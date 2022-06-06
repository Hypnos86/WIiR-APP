# Generated by Django 3.2.9 on 2022-06-06 12:28

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
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Nazwa')),
                ('content', models.TextField(verbose_name='Treść')),
                ('scan', models.FileField(upload_to='commands/%Y/%m/', verbose_name='Skan polecenia')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Data dodania')),
            ],
            options={
                'verbose_name': 'Polecenie',
                'verbose_name_plural': 'Polecenia',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=50, verbose_name='Brażna')),
            ],
            options={
                'verbose_name': 'Branża',
                'verbose_name_plural': 'Branże',
            },
        ),
        migrations.CreateModel(
            name='OrganisationTelephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone_book', models.FileField(null=True, upload_to='KWP_telephone/%Y/', verbose_name='Spis telefonów KWP w Poznaniu')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='Data dodania')),
            ],
            options={
                'verbose_name': 'Książka telefoniczna KWP w Poznaniu',
                'verbose_name_plural': 'Książka telefoniczna KWP w Poznaniu',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, verbose_name='Zespół')),
            ],
            options={
                'verbose_name': 'Komórka Wydziału',
                'verbose_name_plural': 'Komórki Wydziału',
            },
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, default='', max_length=20, verbose_name='Stanowisko')),
                ('fname', models.CharField(blank=True, default='', max_length=15, verbose_name='Imię')),
                ('lname', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Nazwisko')),
                ('no_room', models.CharField(blank=True, default='', max_length=2, verbose_name='Nr. pokoju')),
                ('no_tel_room', models.CharField(blank=True, default='', max_length=6, verbose_name='Nr. telefonu')),
                ('no_tel_private', models.CharField(blank=True, default='', max_length=9, null=True, verbose_name='Nr. komórkowy')),
                ('information', models.CharField(blank=True, max_length=200, null=True, verbose_name='Informacje')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team', verbose_name='Zespół')),
            ],
            options={
                'verbose_name': 'Telefony',
                'verbose_name_plural': 'Telefony',
                'ordering': ['team', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=25, verbose_name='Nazwisko')),
                ('industry_specialist', models.BooleanField(default=0, verbose_name='Branżysta merytoryczny')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.industrytype', verbose_name='Branża')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team', verbose_name='Zespół')),
            ],
            options={
                'verbose_name': 'Pracownik',
                'verbose_name_plural': 'Pracownicy',
                'ordering': ['team', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='AccessModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractors_module', models.BooleanField(default=False, verbose_name='Moduł Kontrahenci')),
                ('contracts_immovables_module', models.BooleanField(default=False, verbose_name='Moduł Umowy Najmu')),
                ('investments_module', models.BooleanField(default=False, verbose_name='Moduł Inwestycje')),
                ('invoices_module', models.BooleanField(default=False, verbose_name='Moduł Faktury')),
                ('cpvdict_module', models.BooleanField(default=False, verbose_name='Moduł Rodzajowość')),
                ('listregister_float_team_module', models.BooleanField(default=False, verbose_name='Moduł Ewidencja: ZM')),
                ('listregister_exploatation_team_module', models.BooleanField(default=False, verbose_name='Moduł Ewidencja: ZE')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessmodule', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Dostęp do modułów',
                'verbose_name_plural': 'Dostęp do modułów',
            },
        ),
    ]
