from django.db import models

import units.models
from units.models import Unit, Powiat


class Stan(models.Model):
    class Meta:
        verbose_name = "Stan umowy"
        verbose_name_plural = "Stany umów"

    stan = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.stan}'


class Rodzaj(models.Model):
    class Meta:
        verbose_name = "Rodzaj umowy"
        verbose_name_plural = "Rodzaje umów"

    rodzaj = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rodzaj}'


class Podstawa(models.Model):
    class Meta:
        verbose_name = "Podstawa prawna"
        verbose_name_plural = "Podstawy prawne"

    podstawa = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.podstawa}'


class Contractimmovables(models.Model):
    class Meta:
        verbose_name = "Umowa nieruchomosci"
        verbose_name_plural = "Umowy nieruchomosci"

    data_umowy = models.DateField("Data umowy")
    nrumowy = models.CharField("Nr umowy", max_length=20, null=True, blank=True, default="")
    kontrahent = models.ForeignKey("contractors.Contractor", on_delete=models.CASCADE, verbose_name="Kontrahent", related_name="contractimmovables")
    podstawa = models.ForeignKey("contracts.Podstawa", on_delete=models.CASCADE, blank=True,
                                 verbose_name="Podstawa prawna", related_name="contractimmovables")
    okres_obowiazywania = models.DateField("Okres obowiązywania", null=True, blank=True)
    rodzaj = models.ForeignKey("contracts.Rodzaj", on_delete=models.CASCADE, verbose_name="Rodzaj umowy", related_name="contractimmovables")
    pow_uzyczona = models.DecimalField("Powierzchnia użytkowa", max_digits=8, decimal_places=2, null=True, blank=True)
    koszt_czynsz = models.BooleanField("Czynsz")
    koszt_prad = models.BooleanField("Prąd")
    koszt_gaz = models.BooleanField("Gaz")
    koszt_woda = models.BooleanField("Woda")
    koszt_co = models.BooleanField("C.O.")
    koszt_smieci = models.BooleanField("Śmieci")
    koszt_podsmiec = models.BooleanField("Zagospodarowanie odpadami komunalnymi")
    koszt_podnier = models.BooleanField("Podatek od nieruchomości")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False, verbose_name="Jednostka", related_name="contractimmovables")
    skan = models.FileField(upload_to='umowy_pdf/%Y/', null=True, blank=True, verbose_name="Skan umowy")
    stan = models.ForeignKey(Stan, on_delete=models.CASCADE, blank=False, default=1, related_name="contractimmovables")
    comments = models.TextField("Informacje", blank=True, default="")
    archives = models.BooleanField("Aktywna", null=False, default=1)
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'Umowa z dnia {self.data_umowy}'


class Aneks(models.Model):
    class Meta:
        verbose_name = "Aneks"
        verbose_name_plural = "Aneksy"
    contract = models.ForeignKey("contracts.Contractimmovables", on_delete=models.CASCADE, related_name="aneks")
    skan_aneksu = models.FileField(upload_to='aneksy_pdf/%Y/', null=True, blank=True, verbose_name="Skan aneks")
    data_aneksu = models.DateField("Data aneksu", null=True)
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data_aneksu} {self.skan_aneksu}'
