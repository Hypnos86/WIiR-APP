# Generated by Django 4.1 on 2023-04-08 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_necesseryfile"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="necesseryfile",
            options={
                "ordering": ["-create_date"],
                "verbose_name": "Plik",
                "verbose_name_plural": "S.09 - Niezbędne pliki",
            },
        ),
        migrations.RemoveField(model_name="necesseryfile", name="author",),
    ]
