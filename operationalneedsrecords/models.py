from django.db import models
from units.models import Unit


# Create your models here.
class RegistrationType(models.Model):
    class Meta:
        verbose_name = "Rodzaj zgłoszenia"
        verbose_name_plural = "Rodzaje zgłoszeń"

    registration_type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.registration_type}'


class MeritsType(models.Model):
    class Meta:
        verbose_name = "Rodzaj merytoryczny"
        verbose_name_plural = "Rodzaje merytoryczne"

    merits_type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.merits_type}'


class NeedsLetter(models.Model):
    class Meta:
        verbose_name = "Ewidencja pism"
        verbose_name_plural = "Ewidencje Pism"

    related_name = "NeedsLetter"

    receipt_date = models.DateField("Data wpływu", null=True)
    case_sign = models.CharField("Znak pisma", max_length=30, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Jednostka", related_name=related_name)
    case_description = models.TextField()
    registration_type = models.ForeignKey(RegistrationType, on_delete=models.CASCADE, verbose_name="Rodzaj zgłoszenia",
                                          related_name=related_name)
    no_secretariats_diary = models.IntegerField("Nr. z dziennika")