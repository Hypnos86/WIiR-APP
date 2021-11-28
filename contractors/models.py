from django.db import models


class Contractor(models.Model):
    nazwa = models.CharField(max_length=30, null=True)
    adres = models.CharField(max_length=30, null=True)
    kod_pocztowy = models.CharField(max_length=6, null=True)
    miasto = models.CharField(max_length=20, null=True)
    informacje = models.TextField(blank=True, default="")
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa}, {self.adres}, {self.kod_pocztowy} {self.miasto}'
