from django.db import models


# Create your models here.
class County(models.Model):
    class Meta:
        verbose_name = "Powiat"
        verbose_name_plural = "J.01 - Powiaty"
        ordering = ["id_order"]

    swop_id = models.CharField(max_length=4, verbose_name="ID SWOP")
    name = models.CharField(max_length=15, null=False, verbose_name="Powiat", unique=True)
    id_order = models.IntegerField("Kolejność", unique=True, null=True)

    def __str__(self):
        return f"{self.name}"


class TypeUnit(models.Model):
    class Meta:
        verbose_name = "Rodzaj jednostki"
        verbose_name_plural = "J.02 - Rodzaje jednostek"
        ordering = ["id"]

    type_short = models.CharField(max_length=10, null=False, verbose_name="Skrócona nazwa")
    type_full = models.CharField(max_length=30, null=False, verbose_name="Pełna nazwa")

    def __str__(self):
        return f"{self.type_short}"


class Unit(models.Model):
    class Meta:
        verbose_name = "Jednostka"
        verbose_name_plural = "J.03 - Jednostki"
        ordering = ["county__name", "type"]

    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="unit", verbose_name="Powiat")
    type = models.ForeignKey(TypeUnit, on_delete=models.CASCADE, related_name="unit", verbose_name="Rodzaj jednostki")
    address = models.CharField(max_length=50, verbose_name="Adres")
    zip_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=40, verbose_name="Miasto")
    information = models.CharField(max_length=200, blank=True, verbose_name="Obiekt")
    manager = models.CharField(max_length=150, verbose_name="Trwały zarząd", default="Policja")
    comments = models.TextField(blank=True, verbose_name="Uwagi")
    status = models.BooleanField(default=True, verbose_name="Aktualna")
    full_name = models.CharField(max_length=250, verbose_name="Pełna nazwa jednostki", null=True, blank=True)
    change = models.DateTimeField(auto_now=True, verbose_name="Zmiany")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="unit", verbose_name="Autor")

    def __str__(self):
        return f"{self.information} - {self.city}, {self.address}"
