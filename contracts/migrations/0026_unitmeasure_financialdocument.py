# Generated by Django 4.1 on 2023-02-04 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cpvdict", "0007_remove_order_unit_order_unit"),
        ("contracts", "0025_alter_guaranteesettlement_script"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnitMeasure",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "measureName",
                    models.CharField(max_length=30, verbose_name="Jednostka miary"),
                ),
            ],
            options={
                "verbose_name": "Jednostka miary",
                "verbose_name_plural": "jednostki miary",
            },
        ),
        migrations.CreateModel(
            name="FinancialDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Data")),
                (
                    "no_document",
                    models.CharField(max_length=30, verbose_name="Nr. dokumentu"),
                ),
                (
                    "value",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Zużycie"
                    ),
                ),
                (
                    "cost_netto",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Kwota netto"
                    ),
                ),
                (
                    "cost_brutto",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Kwota brutto"
                    ),
                ),
                (
                    "information",
                    models.TextField(
                        blank=True, default="", null=True, verbose_name="Informacje"
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data utworzenia"
                    ),
                ),
                ("change", models.DateTimeField(auto_now=True, verbose_name="Zmiany")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="financialdocument",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Autor",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="financialdocument",
                        to="contracts.contractmedia",
                        verbose_name="Uowa",
                    ),
                ),
                (
                    "unit_measure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="financialdocument",
                        to="contracts.unitmeasure",
                        verbose_name="Jednostka miary",
                    ),
                ),
                (
                    "vat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="financialdocument",
                        to="cpvdict.tax",
                        verbose_name="Vat",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dokument księgowy",
                "verbose_name_plural": "Dokumenty księkowe",
                "ordering": ["date"],
            },
        ),
    ]