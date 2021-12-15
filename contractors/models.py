from django.db import models


class Contractor(models.Model):
    class Meta:
        verbose_name = "Kontrahenci"
        verbose_name_plural = "Kontrahenci"
        ordering = ['nazwa']

    nocuntractor = models.CharField("Nr. kontrahenta", max_length=10, null=False, unique=True)
    nazwa = models.CharField("Nazwa", max_length=30, null=True)
    nip = models.CharField("NIP", max_length=10, null=True, blank=True)
    adres = models.CharField("Adres", max_length=30, null=True)
    kod_pocztowy = models.CharField("Kod pocztowy", max_length=6, null=True)
    miasto = models.CharField("Miasto", max_length=20, null=True)
    informacje = models.TextField("Informacje", null=True, blank=True, default="")
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa}, {self.adres}, {self.kod_pocztowy} {self.miasto}'