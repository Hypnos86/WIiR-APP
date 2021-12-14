# Generated by Django 3.2.9 on 2021-12-14 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=2, verbose_name='Grupa')),
                ('name', models.CharField(max_length=50, verbose_name='Nazwa')),
            ],
            options={
                'verbose_name': 'Grupa',
                'verbose_name_plural': 'Grupy',
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(max_length=6, verbose_name='Paragraf')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Nazwa')),
            ],
            options={
                'verbose_name': 'Paragraf i pozycja',
                'verbose_name_plural': 'Paragrafy i pozycje',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=5, verbose_name='Rozdział')),
                ('name', models.CharField(max_length=20, verbose_name='Nazwa')),
            ],
            options={
                'verbose_name': 'Rozdział',
                'verbose_name_plural': 'Rozdziay',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=80, null=True, verbose_name='Źródło')),
            ],
            options={
                'verbose_name': 'Źródło',
                'verbose_name_plural': 'Źródła',
            },
        ),
        migrations.CreateModel(
            name='Financesource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sourcefinancing.group', verbose_name='Grupa')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sourcefinancing.paragraph', verbose_name='Paragraf')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sourcefinancing.section', verbose_name='Rozdział')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sourcefinancing.source', verbose_name='Źródło finansowania')),
            ],
            options={
                'verbose_name': 'Konto',
                'verbose_name_plural': 'Konta',
            },
        ),
    ]
