import os

from django.db import models
from contractors.models import Contractor
from units.models import Unit


# Create your models here.
class TypeDonation(models.Model):
    class Meta:
        verbose_name = 'Rodzaj darowizny'
        verbose_name_plural = 'Rodzaje darowizn'

    type_name = models.CharField('Rodzaj', max_length=40)

    def __str__(self):
        return f'{self.type_name}'


class TypeFinancialResources(models.Model):
    class Meta:
        verbose_name = 'Rodzaj środków'
        verbose_name_plural = 'Rodzaje środków'

    type_name = models.CharField('Rodzaj środków', max_length=40)

    def __str__(self):
        return f'{self.type_name}'


def upload_donation_scan(instance, filename):
    date = instance.date_receipt
    date_agreement = instance.date_agreement
    character = instance.character
    extension = os.path.splitext(filename)
    return f'donations/{date.strftime("%Y")}/{character}/Porozumienie z dnia {date_agreement.strftime("%d.%m.%Y")}{extension}'


class Application(models.Model):
    class Meta:
        verbose_name = 'Wniosek'
        verbose_name_plural = 'Wnioski'
        ordering = ['date_receipt']

    character = models.CharField('Nr. sprawy', max_length=25)
    date_receipt = models.DateField("Data wpływu")
    date_return = models.DateField('Data zwrotu')
    no_application = models.CharField('Nr. wniosku', max_length=10)
    no_agreement = models.CharField('Nr. porozumienia', max_length=25, null=True, blank=True)
    date_agreement = models.DateField('Data porozumienia')
    donation_type = models.ForeignKey(TypeDonation, on_delete=models.CASCADE, verbose_name='Rodzaj darowizny',
                                      related_name='application')
    financial_type = models.ForeignKey(TypeFinancialResources, on_delete=models.CASCADE, verbose_name='Rodzaj środków',
                                       null=True, blank=True, related_name='application')
    presenter = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name='Darczyńca',
                                  related_name='application')
    sum = models.DecimalField('Kwota darowizny', max_digits=10, decimal_places=2, null=True, blank=True)
    settlement_date = models.DateField('Data rozliczenia')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Jednostka', related_name='application')
    subject = models.TextField('Przedmiot porozumienia', null=True, blank=True)
    information = models.TextField('Informacje', null=True, blank=True, default="")
    donation_scan = models.FileField(upload_to=upload_donation_scan, null=True, blank=True,
                                     verbose_name='Skan porozumienia')
    creation_date = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Autor', related_name='application')

    def __str__(self):
        return f'{self.no_application}'
