from django.db import models
from contractors.models import Contractor
from contracts.models import ContractImmovables


# Create your models here.

class Creator(models.Model):
    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Wystawcy faktur - sprzedaż"

    creator = models.CharField("Pracownik",max_length=20)

    def __str__(self):
        return f'{self.creator}'


class Invoiceitems(models.Model):
    class Meta:
        verbose_name = "Element faktury"
        verbose_name_plural = "Elementy faktury"

    acount = models.ForeignKey("sourcefinancing.Financesource", on_delete=models.CASCADE, verbose_name="Konto",
                               related_name="invoiceitems")
    powiat = models.ForeignKey("units.Powiat", on_delete=models.CASCADE, verbose_name="Powiat",
                               related_name='invoiceitems')
    sum = models.DecimalField("Kwota [zł]", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.acount}{self.powiat} - {self.sum} zł.'


# class Year(models.Model):
#     year = models.DateField(Year)

class Invoicesell(models.Model):
    class Meta:
        verbose_name = "Faktura sprzedaży"
        verbose_name_plural = "Faktury - sprzedaż"

    data = models.DateField("Data wystawienia")
    noinvoice = models.CharField("Nr. faktury", max_length=11)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name='invoicesell')
    sum = models.DecimalField("Kwota", max_digits=10, decimal_places=2, null=True, blank=True)
    powiat = models.ForeignKey("units.Powiat", on_delete=models.CASCADE, verbose_name="Powiat",
                               related_name='invoicesell')
    period_from = models.DateField("Okres od")
    period_to = models.DateField("Okres do")
    creator = models.ForeignKey("invoices.Creator", on_delete=models.CASCADE, verbose_name="Osoba wystawiająca",
                                related_name='invoicesell')
    comments = models.TextField("Informacje", blank=True, default="")
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='invoicebuy')

    def __str__(self):
        return f'Faktura nr {self.noinvoice} z dnia {self.data} na kwotę {self.sum} zł.'


class Invoicebuy(models.Model):
    class Meta:
        verbose_name = "Faktura - kupno"
        verbose_name_plural = "Faktury - kupno"

    datawyplytu = models.DateField("Data wypływu")
    data = models.DateField("Data wystawienia")
    noinvoice = models.CharField("Nr. faktury", max_length=30)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name='invoicebuy')
    invoiceitems = models.ForeignKey(Invoiceitems, on_delete=models.CASCADE, related_name="invoiceitems",
                                     verbose_name="Źródło finansowania")
    period_from = models.DateField("Okres od")
    period_to = models.DateField("Okres do")

    comments = models.TextField("Informacje", blank=True, default="")
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='invoicesell')

    def __str__(self):
        return f'Faktura nr. {self.noinvoice} z dnia {self.data}, na kwotę {self.invoiceitems}'
