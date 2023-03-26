from django.db import models


# Create your models here.
class OfficialFlat(models.Model):
    class Meta:
        verbose_name = "Mieszkanie służbowe"
        verbose_name_plural = "M.01 - Mieszkania służbowe"

    related_name = "officialflat"

    address = models.CharField("Adres", max_length=150)
    zip_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=40, verbose_name="Miasto")
    area = models.DecimalField("Powierzchnia", max_digits=5, decimal_places=2, null=True, blank=True)
    room_numbers = models.IntegerField("Ilość pomieszczeń", null=True, blank=True)
    flor = models.IntegerField("Piętro", null=True, blank=True)
    state = models.BooleanField("Wolne", default=True)
    information = models.TextField("Informacje", null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=related_name,
                               verbose_name="Autor")

    def __str__(self):
        return f"Mieszkanie służbowe: {self.address}, {self.city}"
