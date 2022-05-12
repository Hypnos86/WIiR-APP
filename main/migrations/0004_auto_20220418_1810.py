# Generated by Django 3.2.9 on 2022-04-18 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220418_0955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='industrytype',
            options={'verbose_name': 'Branża', 'verbose_name_plural': 'Branże'},
        ),
        migrations.AddField(
            model_name='employer',
            name='industry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.industrytype', verbose_name='Branża'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='industry_specialist',
            field=models.BooleanField(default=0, verbose_name='Branżysta merytoryczny'),
        ),
    ]