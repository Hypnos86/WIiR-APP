from django.db import models
from units.models import Unit


class KindBuilding(models.Model):
    class Meta:
        verbose_name = "Rodzaj budynku"
        verbose_name_plural = "Rodzaje budynkuów"
        ordering = ["kind"]

    kind = models.CharField("Rodzaj", max_length=50)

    def __str__(self):
        return f"{self.kind}"


# Create your models here.
class Building(models.Model):
    class Meta:
        verbose_name = "Budynek"
        verbose_name_plural = "Budynki"

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Jednostka", related_name="building")
    no_inventory = models.CharField("Nr. inwentarzowy", max_length=20, unique=True)
    building_name = models.CharField("Nazwa obiektu", max_length=100)
    kind = models.ForeignKey(KindBuilding, on_delete=models.CASCADE, verbose_name="Rodzaj budynku",
                             related_name="building")
    usable_area = models.DecimalField("Powierzchnia użytkowa", max_digits=6, decimal_places=2, null=True, blank=True)
    volume = models.DecimalField("Kubatura", max_digits=8, decimal_places=2, null=True, blank=True)
    information = models.TextField("Informacje", null=True, blank=True, default="")
    state = models.BooleanField("Aktywny", default=True)
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="building",
                               verbose_name="Autor")

    def __str__(self):
        return f"{self.no_inventory} - {self.kind}"
