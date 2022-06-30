# Generated by Django 4.0.5 on 2022-06-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_employer_information_employer_no_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='main.industrytype', verbose_name='Branża'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='main.team', verbose_name='Zespół'),
        ),
        migrations.DeleteModel(
            name='Telephone',
        ),
    ]
