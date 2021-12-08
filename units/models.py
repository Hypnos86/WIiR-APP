from django.db import models


# Create your models here.
class Powiat(models.Model):
    class Meta:
        verbose_name = "Powiat"
        verbose_name_plural = "Powiaty"

    swop_id = models.CharField(max_length=4)
    powiat = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f'{self.powiat}'


class Rodzaj(models.Model):
    class Meta:
        verbose_name = "Rodzaj jednostki"
        verbose_name_plural = "Rodzaje jednostek"
    rodzaj = models.CharField(max_length=10, null=False)

    def __str__(self):
        return f'{self.rodzaj}'


class Unit(models.Model):
    class Meta:
        verbose_name = "Jednostka"
        verbose_name_plural = "Jednostki"

    powiat = models.ForeignKey(Powiat, on_delete=models.CASCADE)
    rodzaj = models.ForeignKey(Rodzaj, on_delete=models.CASCADE)
    adres = models.CharField(max_length=30)
    kod_pocztowy = models.CharField(max_length=6)
    miasto = models.CharField(max_length=20)
    informacje = models.TextField(blank=True)
    aktywna = models.BooleanField("Aktywna", null=False, default=0)

    def __str__(self):
        return f'{self.informacje} {self.miasto}, {self.adres} ({self.powiat})'
