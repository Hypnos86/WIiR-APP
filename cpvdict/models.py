from django.db import models
from units.models import Unit


# Create your models here.
class Typecpv(models.Model):
    class Meta:
        verbose_name = "CPV"
        verbose_name_plural = "Słownik CPV"

    no_cpv = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.no_cpv}'


class TypeOrder(models.Model):
    class Meta:
        verbose_name = "Rodzaj zamowienia"
        verbose_name_plural = "Rodzaj zamówienia"

    type = models.CharField("Rodzaj zamówienia", max_length=20, null=True)

    def __str__(self):
        return {self.type}


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


class Order(models.Model):
    class Meta:
        verbose_name = "Zlecenie/Umowa"
        verbose_name_plural = "Zlecenia/Umowy"

    date = models.DateField("Data")
    no_order = models.CharField("Nr zlecenia", max_length=15)
    sum = models.DecimalField("Szacowana kwota", max_digits=8, decimal_places=2, null=True, blank=True)
    type = models.ForeignKey(TypeOrder, on_delete=models.CASCADE, verbose_name="Rodzaj zamówienia",
                             related_name="Order")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False, verbose_name="Obiekt",
                             related_name="Order")
    brakedown = models.BooleanField("Awaria", default=1)

    def __str__(self):
        return f'Zlecenie nr {self.no_order} z dnia {self.date} (rodzaj: {self.type}'
