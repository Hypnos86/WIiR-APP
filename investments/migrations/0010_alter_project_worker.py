# Generated by Django 3.2.9 on 2022-05-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_command_scan'),
        ('investments', '0009_auto_20220517_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='worker',
            field=models.ManyToManyField(null=True, related_name='project', to='main.Employer', verbose_name='Odpowiedzialny'),
        ),
    ]
