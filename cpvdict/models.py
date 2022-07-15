from django.db import models
from units.models import Unit
from contractors.models import Contractor
from main.models import Employer


# Create your models here.
class Typecpv(models.Model):
    class Meta:
        verbose_name = "CPV"
        verbose_name_plural = "Słownik CPV"

    no_cpv = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.no_cpv}'


class TypeOrder(models.Model):
    class Meta:
        verbose_name = "Rodzaj zamowienia"
        verbose_name_plural = "Rodzaj zamówienia"

    type = models.CharField("Rodzaj zamówienia", max_length=20, null=True)

    def __str__(self):
        return f'{self.type}'


class Genre(models.Model):
    class Meta:
        verbose_name = "Przedmiot zamówienia"
        verbose_name_plural = "Klasyfikacja rodzajowa"
        ordering = ['name_id']

    name_id = models.CharField("ID", max_length=4, unique=True)
    name = models.CharField("Ogólna nazwa przedmiotu zamówienia w ujęciu rodzajowym", max_length=200)
    cpv = models.ManyToManyField("cpvdict.Typecpv", verbose_name="Kody CPV", related_name="Genre")
    sum = models.DecimalField("Suma zamówień", max_digits=8, decimal_places=2, null=True, blank=True)
    remain = models.DecimalField("Pozostało", max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'({self.name_id}) {self.name}'


class Tax(models.Model):
    class Meta:
        verbose_name = 'Podatek Vat'
        verbose_name_plural = 'Rodzaje podatków vat'

    vat = models.SmallIntegerField('Podatek [%]', default=0)

    def __str__(self):
        return f'{self.vat}%'


class OrderLimit(models.Model):
    class Meta:
        verbose_name = "Limit zamówień"
        verbose_name_plural = "Limit zamówień"
        ordering = ['-year']

    year = models.IntegerField('Rok', unique=True)
    euro_exchange_rate = models.DecimalField('Kurs euro', max_digits=5, decimal_places=4)
    limit_euro = models.DecimalField('Limit euro', max_digits=10, decimal_places=2)
    limit_netto = models.DecimalField('Limit zamówień netto', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.year} - {self.euro_exchange_rate} ({self.limit_euro}) - {self.limit_netto}zł.'


class Order(models.Model):
    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"
        ordering = ['-date']

    date = models.DateField('Data')
    no_order = models.CharField('Nr zlecenia', max_length=15, blank=True, default="", unique=True)
    sum_netto = models.DecimalField('Kwota netto', max_digits=8, decimal_places=2)
    vat = models.ForeignKey(Tax, on_delete=models.CASCADE, verbose_name='Podatek', related_name='order')
    sum_brutto = models.DecimalField('Kwota brutto', max_digits=10, decimal_places=2, null=True, blank=True)
    typeorder = models.ForeignKey(TypeOrder, on_delete=models.CASCADE, verbose_name="Rodzaj zamówienia",
                                  related_name="order")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="order", verbose_name="ID rodzajowości")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name='Kontrahent',
                                   related_name='order')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False, verbose_name="Obiekt",
                             related_name="order")
    brakedown = models.BooleanField("Awaria")
    worker = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name='Branżysta', related_name='order')
    content = models.TextField("Zakres", blank=True, default="")
    create_date = models.DateField('Data dodania', auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="order")

    def __str__(self):
        return f'Zlecenie nr {self.no_order} z dnia {self.date} (rodzaj: {self.typeorder})'
