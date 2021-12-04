from django.db import models


# Create your models here.
class Team(models.Model):
    class Meta:
        verbose_name = "Komórka Wydziału"
        verbose_name_plural = "Komórki Wydziału"

    team = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.team}'


class Telephone(models.Model):
    class Meta:
        verbose_name = "Telefony"
        verbose_name_plural = "Telefony"

    team = models.ForeignKey("main.Team", on_delete=models.CASCADE)
    position = models.CharField("Stanowisko", max_length=20, blank=True, default="")
    fname = models.CharField("Imię", max_length=15, blank=True, default="")
    lname = models.CharField("Nazwisko", max_length=15, null=True, blank=True, default="")
    numbtelbus = models.CharField("Nr. telefonu", max_length=6, blank=True, default="")
    numbtelpri = models.CharField("Nr. komórkowy", max_length=9, null=True, blank=True, default="")

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.position}. Tel: {self.numbtelbus}'
