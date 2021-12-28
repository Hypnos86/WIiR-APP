from django.db import models


# Create your models here.
class Typecpv(models.Model):
    class Meta:
        verbose_name = "CPV"
        verbose_name_plural = "Słownik CPV"

    nocpv = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nocpv}'


class OrderingObject(models.Model):
    class Meta:
        verbose_name = "Przedmiot zamówienia"
        verbose_name_plural = "Klasyfikacja rodzajowa"
        ordering = ['name_id']

    name_id = models.CharField("ID", max_length=4, unique=True)
    name = models.CharField("Ogólna nazwa przedmiotu zamówienia w ujęciu rodzajowym", max_length=200)
    cpv = models.ManyToManyField("cpvdict.Typecpv", verbose_name="Kody CPV", related_name="OrderingObject")

    # usedSum = models.DecimalField("Wykorzystano", max_digits=10, decimal_places=2)
    # leftSum = models.DecimalField("Wykorzystano", max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
