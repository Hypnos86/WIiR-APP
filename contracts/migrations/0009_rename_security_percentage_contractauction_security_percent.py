# Generated by Django 3.2.9 on 2022-01-10 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_auto_20220110_0943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contractauction',
            old_name='security_percentage',
            new_name='security_percent',
        ),
    ]