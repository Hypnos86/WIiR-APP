from django.db import models
from polymorphic.models import PolymorphicModel
from fixedasset.models import Building


# Create your models here.
class TypeInspection(models.Model):
    class Meta:
        verbose_name = "Rodzaj przeglądu"
        verbose_name_plural = "Rodzaje przeglądu"

    inspection_name = models.CharField("Rodzaj przeglądu", max_length=50)

    def __str__(self):
        return f"{self.inspection_name}"


class TechnicalCondition(models.Model):
    class Meta:
        verbose_name = "Stan tehcniczny"
        verbose_name_plural = "Rodzaje stanów technicznych"
        ordering = ["ordinal_number"]

    ordinal_number = models.SmallIntegerField("Liczba porządkowa", unique=True)
    condition = models.CharField("Stan tehcniczny", max_length=30)

    def __str__(self):
        return {self.condition}


class PatternInspections(PolymorphicModel):
    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name="patterninspections")
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name="patterninspections")
    date_protocol = models.DateField("Data protokołu")
    conclusions = models.TextField("Wnioski")
    date_next_inspection = models.DateField("Data kolejnego przeglądu")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="patterninspections",
                               verbose_name="Autor")


class BuildingInspectionOneYear(PatternInspections):
    class Meta:
        verbose_name = "Przedląd budynku tehcniczny - roczny"
        verbose_name_plural = "Przeglądy budynków - roczne"
        ordering = []

    def __str__(self):
        return f"{self.date_protocol} - {self.no_inventory}"


class BuildingInspectionFiveYear(PatternInspections):
    class Meta:
        verbose_name = "Przedląd budynku tehcniczny - pięcioletni"
        verbose_name_plural = "Przeglądy budynków - pięcioletni"
        ordering = []

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ChimneyInspection(PatternInspections):
    class Meta:
        verbose_name = "Przedląd komina"
        verbose_name_plural = "Przeglądy kominów"
        ordering = []

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'
