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
        verbose_name = "Stan techniczny"
        verbose_name_plural = "Rodzaje stanów technicznych"
        ordering = ["ordinal_number"]

    ordinal_number = models.SmallIntegerField("Liczba porządkowa", unique=True)
    condition = models.CharField("Stan techniczny", max_length=30)

    def __str__(self):
        return {self.condition}


class PatternInspections(PolymorphicModel):
    class Meta:
        ordering = ["date_protocol"]

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name="patterninspections")
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name="patterninspections")
    date_protocol = models.DateField("Data protokołu")
    conclusions = models.TextField("Wnioski")
    date_next_inspection = models.DateField("Data kolejnego przeglądu", null=True, blank=True)
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="patterninspections",
                               verbose_name="Autor")


class BuildingInspectionOneYear(PatternInspections):
    class Meta:
        verbose_name = "Przegląd budynku techniczny - roczny"
        verbose_name_plural = "Przeglądy budynków - roczny"

    def __str__(self):
        return f"{self.date_protocol} - {self.no_inventory}"


class BuildingInspectionFiveYear(PatternInspections):
    class Meta:
        verbose_name = "Przegląd budynku techniczny - pięcioletni"
        verbose_name_plural = "Przeglądy budynków - pięcioletni"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ChimneyInspection(PatternInspections):
    class Meta:
        verbose_name = "Przegląd komina"
        verbose_name_plural = "Przeglądy kominów"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ElectricalInspectionOneYear(PatternInspections):
    class Meta:
        verbose_name = "Przedląd elektryczny - roczny"
        verbose_name_plural = "Przeglądy elektryczne - roczny"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ElectricalInspectionFiveYear(PatternInspections):
    class Meta:
        verbose_name = "Przedląd elektryczny - pięcioletni"
        verbose_name_plural = "Przeglądy elektryczne - pięcioletni"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class HeatingBoilerInspection(PatternInspections):
    class Meta:
        verbose_name = "Przegląd kotła grzewczego"
        verbose_name_plural = "Przeglądy kotłów grzewczych"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class AirConditionerInspection(PatternInspections):
    class Meta:
        verbose_name = "Przegląd klimatyzatora"
        verbose_name_plural = "Przeglądy klimatyzatorów"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class FireInspection(PatternInspections):
    class Meta:
        verbose_name = "Przegląd przeciwpożarowy"
        verbose_name_plural = "Przeglądy przeciwpożarowe"

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'
