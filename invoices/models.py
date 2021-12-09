from django.db import models
from contractors.models import Contractorsell
from contracts.models import Contractimmovables


# Create your models here.

class Creator(models.Model):
    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Wystawcy faktur - sprzedaż"

    creator = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.creator}'


class Invoicesell(models.Model):
    class Meta:
        verbose_name = "Faktura sprzedaży"
        verbose_name_plural = "Faktury - sprzedaż"

    data = models.DateField("Data wystawienia")
    noinvoice = models.CharField("Nr. faktury", max_length=11)
    contractor = models.ForeignKey(Contractorsell, on_delete=models.CASCADE, verbose_name="Kontrahent")
    sum = models.DecimalField("Kwota", max_digits=10, decimal_places=2, null=True, blank=True)
    powiat = models.ForeignKey("units.Powiat", on_delete=models.CASCADE, verbose_name="Powiat")
    period_from = models.DateField("Okres od")
    period_to = models.DateField("Okres do")
    creator = models.ForeignKey("invoices.Creator", on_delete=models.CASCADE, verbose_name="Osoba wystawiająca")
    comments = models.TextField("Informacje", blank=True, default="")
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'Faktura nr {self.noinvoice} z dnia {self.data} na kwotę {self.sum} zł.'
