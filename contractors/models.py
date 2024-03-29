from django.db import models


class Contractor(models.Model):
    class Meta:
        verbose_name = "Kontrahenci"
        verbose_name_plural = "K.01 - Kontrahenci"
        ordering = ["name"]
        unique_together = ["no_contractor", "nip"]

    no_contractor = models.IntegerField("Nr. kontrahenta", null=True, blank=True, unique=True, default="")
    name = models.CharField("Nazwa", max_length=100, null=True)
    nip = models.CharField("NIP", max_length=10, null=True, blank=True, unique=True)
    address = models.CharField("Adres", max_length=30, null=True)
    zip_code = models.CharField("Kod pocztowy", max_length=6, null=True)
    city = models.CharField("Miasto", max_length=20, null=True)
    information = models.TextField("Informacje", null=True, blank=True, default="")
    slug = models.SlugField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField("Zmiany", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return f"{self.name}, {self.address}, {self.zip_code} {self.city} ({self.no_contractor})"
