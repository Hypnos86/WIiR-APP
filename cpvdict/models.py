from django.db import models


# Create your models here.
class Typecpv(models.Model):
    class Meta:
        verbose_name = "CPV"
        verbose_name_plural = "Słownik CPV"
    nocpv = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
