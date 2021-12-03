from django.db import models


class Contractorsell(models.Model):
    class Meta:
        verbose_name = "Kontrahenci - sprzedaż"
        verbose_name_plural = "Kontrahenci - sprzedaż"

    nazwa = models.CharField(max_length=30, null=True)
    nip = models.CharField("NIP", max_length=10, null=True)
    adres = models.CharField(max_length=30, null=True)
    kod_pocztowy = models.CharField(max_length=6, null=True)
    miasto = models.CharField(max_length=20, null=True)
    informacje = models.TextField(null=True, blank=True, default="")
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa}, {self.adres}, {self.kod_pocztowy} {self.miasto}'


class Contractorbuy(models.Model):
    class Meta:
        verbose_name = "Kontrahenci - kupno"
        verbose_name_plural = "Kontrahenci - kupno"

    nazwa = models.CharField(max_length=30, null=True)
    nip = models.CharField("NIP", max_length=10, null=True)
    adres = models.CharField(max_length=30, null=True)
    kod_pocztowy = models.CharField(max_length=6, null=True)
    miasto = models.CharField(max_length=20, null=True)
    informacje = models.TextField(null=True, blank=True, default="")
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa}, {self.adres}, {self.kod_pocztowy} {self.miasto}'
