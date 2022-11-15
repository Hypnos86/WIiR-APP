from django.db import models
from polymorphic.models import PolymorphicModel
from fixedasset.models import Building
from tinymce import models as tinymce_models


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
    condition = models.CharField("Klasyfikacja stanu technicznego", max_length=30)
    component_use = models.CharField("Procent zużycia elementu", max_length=9)

    def __str__(self):
        return f"{self.condition}"


class PatternInspections(PolymorphicModel):
    class Meta:
        ordering = ["date_protocol"]

    date_protocol = models.DateField("Data protokołu")
    conclusions = tinymce_models.HTMLField("Wnioski")
    date_next_inspection = models.DateField("Data kolejnego przeglądu", null=True, blank=True)
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)


class BuildingInspectionOneYear(PatternInspections):
    relatedName = "building_inspection_one_year"

    class Meta:
        verbose_name = "Przegląd budynku techniczny - roczny"
        verbose_name_plural = "Przeglądy budynków - roczny"
        ordering = ["no_inventory__unit__county__swop_id"]

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f"{self.date_protocol} - {self.no_inventory}"


class BuildingInspectionFiveYear(PatternInspections):
    relatedName = "building_inspection_five_year"

    class Meta:
        verbose_name = "Przegląd budynku techniczny - pięcioletni"
        verbose_name_plural = "Przeglądy budynków - pięcioletni"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ChimneyInspection(PatternInspections):
    relatedName = "chimney_inspection"

    class Meta:
        verbose_name = "Przegląd komina"
        verbose_name_plural = "Przeglądy kominów"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ElectricalInspectionOneYear(PatternInspections):
    relatedName = "electrical_inspection_one_year"

    class Meta:
        verbose_name = "Przedląd elektryczny - roczny"
        verbose_name_plural = "Przeglądy elektryczne - roczny"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class ElectricalInspectionFiveYear(PatternInspections):
    relatedName = "electrical_inspection_five_year"

    class Meta:
        verbose_name = "Przedląd elektryczny - pięcioletni"
        verbose_name_plural = "Przeglądy elektryczne - pięcioletni"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class HeatingBoilerInspection(PatternInspections):
    relatedName = "heating_boiler_inspection"

    class Meta:
        verbose_name = "Przegląd kotła grzewczego"
        verbose_name_plural = "Przeglądy kotłów grzewczych"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class AirConditionerInspection(PatternInspections):
    relatedName = "air_conditioner_inspection"

    class Meta:
        verbose_name = "Przegląd klimatyzatora"
        verbose_name_plural = "Przeglądy klimatyzatorów"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'


class FireInspection(PatternInspections):
    relatedName = "fire_inspection"

    class Meta:
        verbose_name = "Przegląd przeciwpożarowy"
        verbose_name_plural = "Przeglądy przeciwpożarowe"

    no_inventory = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Obiekt",
                                     related_name=relatedName)
    inspection_name = models.ForeignKey(TypeInspection, on_delete=models.CASCADE, verbose_name="Rodzaj przeglądu",
                                        related_name=relatedName)
    technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, related_name=relatedName,
                                            verbose_name="Stan techniczny")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName,
                               verbose_name="Autor")

    def __str__(self):
        return f'{self.date_protocol} - {self.no_inventory}'
