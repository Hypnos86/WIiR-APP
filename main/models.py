from django.db import models


# Create your models here.
class Telephone(models.Model):
    team = models.CharField("Zespół", max_length=50)
    position = models.CharField("Stanowisko", max_length=20)
    fname = models.CharField("Imię", max_length=15)
    lname = models.CharField("Nazwisko", max_length=15, null=True)
    numbtelbus = models.CharField("Nr. telefonu", max_length=6)
    numbtelpri = models.CharField("Nr. komórkowy", max_length=9, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.position}. Tel: {self.numbtelbus}'