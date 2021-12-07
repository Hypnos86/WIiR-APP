from django.db import models
from contractors.models import Contractorsell
from contracts.models import Contractimmovables


# Create your models here.
class Creator(models.Model):
    class Meta:
        verbose_name = "Wystawcy faktur"
        verbose_name_plural = "Pracownik"
    creator = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.creator}'


class Invoicesell(models.Model):
    class Meta:
        verbose_name = "Faktury"
        verbose_name_plural = "Faktura"

    data = models.DateField("Data wystawienia")
    noinvoice = models.CharField("Nr. faktury", max_length=11)
    contractor = models.ForeignKey(Contractorsell, on_delete=models.CASCADE, verbose_name="Kontrahent")
    sum = models.DecimalField("Kwota", max_digits=4, decimal_places=2, null=True, blank=True)
    contract = models.ForeignKey(Contractimmovables, on_delete=models.CASCADE, verbose_name="Umowa", null=True,
                                     blank=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, verbose_name="Osoba wystawiająca")
    comments = models.TextField("Informacje", blank=True, default="")
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    uzytkownik = models.ForeignKey("auth.User", editable=False,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Faktura nr {self.noinvoice} z dnia {self.data} na kwote {self.sum}'

