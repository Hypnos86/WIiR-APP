from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.
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
    no_inventory = models.CharField(max_length=15, unique=True)
    date_protocol = models.DateField("Data protokołu")
    conclusions = models.TextField("Wnioski")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="patterninspections",
                               verbose_name="Autor")