# Generated by Django 4.0.5 on 2022-07-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_contractmedia_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmedia',
            name='content',
            field=models.CharField(default=1, max_length=100, verbose_name='Treść'),
            preserve_default=False,
        ),
    ]
