# Generated by Django 3.2.9 on 2022-01-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0025_alter_aneksimmovables_data_aneksu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aneksimmovables',
            name='skan_aneksu',
            field=models.FileField(null=True, upload_to='contracts_immovables/annexes/%Y/', verbose_name='Skan aneks'),
        ),
    ]
