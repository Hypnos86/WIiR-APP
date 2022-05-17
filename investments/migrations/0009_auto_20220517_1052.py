# Generated by Django 3.2.9 on 2022-05-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_command_scan'),
        ('investments', '0008_project_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='worker',
        ),
        migrations.AddField(
            model_name='project',
            name='worker',
            field=models.ManyToManyField(related_name='project', to='main.Employer', verbose_name='Odpowiedzialny'),
        ),
    ]
