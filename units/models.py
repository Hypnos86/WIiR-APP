from django.db import models


# Create your models here.
class Powiat(models.Model):
    class Meta:
        verbose_name = "Powiat"
        verbose_name_plural = "Powiaty"
        ordering = ['swop_id']

    swop_id = models.CharField(max_length=4, unique=True)
    powiat = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f'{self.powiat}'


class UnitKind(models.Model):
    class Meta:
        verbose_name = "Rodzaj jednostki"
        verbose_name_plural = "Rodzaje jednostek"

    unit_kind = models.CharField(max_length=10, null=False)

    def __str__(self):
        return f'{self.unit_kind}'


class Unit(models.Model):
    class Meta:
        verbose_name = "Jednostka"
        verbose_name_plural = "Jednostki"

    powiat = models.ForeignKey(Powiat, on_delete=models.CASCADE, related_name="unit")
    unit_kind = models.ForeignKey(UnitKind, on_delete=models.CASCADE, related_name="unit", verbose_name="Rodzaj")
    address = models.CharField('Adres', max_length=30)
    kod_pocztowy = models.CharField('Kod pocztowy', max_length=6)
    miasto = models.CharField('miasto', max_length=20)
    informacje = models.TextField('Informacje', blank=True)
    owner = models.CharField('Właściciel', max_length=50)
    aktywna = models.BooleanField("Aktywna", null=False, default=0)

    def __str__(self):
        return f'{self.informacje} {self.miasto}, {self.address}'
