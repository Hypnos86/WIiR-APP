from django.db import models
from units.models import Unit
from main.models import Employer


# Create your models here.
class RegistrationType(models.Model):
    class Meta:
        verbose_name = "Rodzaj zgłoszenia"
        verbose_name_plural = "Rodzaje zgłoszeń"
        ordering = ["registration_type"]

    registration_type = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.registration_type}'


class MetricsCaseType(models.Model):
    class Meta:
        verbose_name = "Kategoria sprawy"
        verbose_name_plural = "Kategorie spraw"
        ordering = ["metric_type"]

    metric_type = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.metric_type}'


class NeedsLetter(models.Model):
    class Meta:
        verbose_name = "Ewidencja pism"
        verbose_name_plural = "Ewidencje Pism"

    related_name = "needsletter"

    receipt_date = models.DateField("Data wpływu", null=True)
    case_sign = models.CharField("Znak pisma", max_length=30, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Jednostka", related_name=related_name)
    case_description = models.TextField("Opis sprawy")
    case_type = models.ForeignKey(MetricsCaseType, on_delete=models.CASCADE, related_name=related_name,
                                  verbose_name="Rodzaj sprawy")
    registration_type = models.ForeignKey(RegistrationType, on_delete=models.CASCADE, verbose_name="Rodzaj zgłoszenia",
                                          related_name=related_name)
    no_secretariats_diary = models.IntegerField("Nr. z dziennika", unique=True)
    receipt_date_to_team = models.DateField("Data wpływu do Zespołu", null=False, blank=True)
    case_sign_team = models.CharField("Znak sprawy WiiR", max_length=30, null=True, blank=True)
    cost = models.DecimalField(verbose_name="Koszt realizacji", max_digits=10, decimal_places=2, null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name="Branżysta", related_name=related_name)
    execution_date = models.DateField("Data realizacji", null=True, blank=True)
    isDone = models.BooleanField("Zrealizowane")
    information = models.TextField(verbose_name="Informacje", blank=True)
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=related_name, verbose_name="Autor")

    def __str__(self):
        return f'{self.case_sign} z dnia {self.receipt_date}'
