# Generated by Django 4.1 on 2022-10-20 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructioninspections', '0015_alter_technicalcondition_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricalInspectionOneYear',
            fields=[
                ('patterninspections_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='constructioninspections.patterninspections')),
            ],
            options={
                'verbose_name': 'Przedląd elektryczny - roczny',
                'verbose_name_plural': 'Przeglądy elektryczne - roczny',
            },
            bases=('constructioninspections.patterninspections',),
        ),
        migrations.RenameModel(
            old_name='ElectricalInspection',
            new_name='ElectricalInspectionFiveYear',
        ),
        migrations.AlterModelOptions(
            name='electricalinspectionfiveyear',
            options={'verbose_name': 'Przedląd elektryczny - pięcioletni', 'verbose_name_plural': 'Przeglądy elektryczne - pięcioletni'},
        ),
    ]
