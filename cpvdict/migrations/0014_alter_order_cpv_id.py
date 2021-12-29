# Generated by Django 3.2.9 on 2021-12-29 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpvdict', '0013_alter_order_brakedown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cpv_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order', to='cpvdict.genre', verbose_name='ID rodzajowości'),
        ),
    ]
