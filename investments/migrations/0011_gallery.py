# Generated by Django 3.2.9 on 2022-05-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0010_alter_project_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='Gallery/{Project}/%Y/%m')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='investments.project', verbose_name='Id inwestycji')),
            ],
        ),
    ]