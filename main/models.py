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
    numbroom = models.CharField("Nr. pokoju", max_length=2, blank=True, default="")
    numbtelbus = models.CharField("Nr. telefonu", max_length=6, blank=True, default="")
    numbtelpri = models.CharField("Nr. komórkowy", max_length=9, null=True, blank=True, default="")
    information = models.CharField("Informacje", max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.position}. Tel: {self.numbtelbus}'


class OrganisationTelephone(models.Model):
    class Meta:
        verbose_name = "Książka telefoniczna KWP w Poznaniu"
        verbose_name_plural = "Książka telefoniczna KWP w Poznaniu"

    telephone_book = models.FileField(upload_to='KWP_telephone/%Y/', null=True,
                                      verbose_name="Spis telefonów KWP w Poznaniu")
    add_date = models.DateField("Data dodania", auto_now_add=True)


class IndustryType(models.Model):
    class Meta:
        verbose_name = 'Branża'
        verbose_name_plural = 'Branże inspektorów'

    industry = models.CharField('Brażna', max_length=50)

    def __str__(self):
        return f'{self.industry}'


class Inspector(models.Model):
    class Meta:
        verbose_name = 'Inspektor'
        verbose_name_plural = 'Inspektorzy'

    name = models.CharField('Imię', max_length=20)
    last_name = models.CharField('Nazwisko', max_length=25)
    industry = models.ForeignKey(IndustryType, on_delete=models.CASCADE, verbose_name='Branża',
                                 related_name='inspector')

    def __str__(self):
        return f'{self.name} {self.last_name}'
