from django.db import models
from contractors.models import Contractor
from units.models import County
from sourcefinancing.models import FinanceSource


# def year_choises():
#     return [(r, r) for r in range(2019, datetime.date.today().year)]
#
#
# def current_year():
#     return datetime.date.today().year


# class BudgetYear(models.Model, models.Choices):
#     class Meta:
#         verbose_name = "Rok budżetowy"
#         verbose_name_plural = "Lata budżetowe"
#
#     year = models.SmallIntegerField(choices=year_choises, default=current_year)


class Creator(models.Model):
    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Wystawcy faktur - sprzedaż"

    creator = models.CharField("Pracownik", max_length=20)

    def __str__(self):
        return f'{self.creator}'


class InvoiceSell(models.Model):
    class Meta:
        verbose_name = "Faktura sprzedaży"
        verbose_name_plural = "Faktury - sprzedaż"
        ordering = ['-date']

    date = models.DateField("Data wystawienia")
    no_invoice = models.CharField("Nr. faktury", max_length=11)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name='invoicesell')
    sum = models.DecimalField("Kwota [zł]", max_digits=10, decimal_places=2, null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="Powiat", related_name='invoicesell')
    date_of_payment = models.DateField("Termin płatności")
    period_from = models.DateField("Okres od")
    period_to = models.DateField("Okres do")
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, verbose_name="Osoba wystawiająca",
                                related_name='invoicesell')
    information = models.TextField("Informacje", blank=True, default="")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change_date = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='invoicesell')

    def __str__(self):
        return f'Faktura nr {self.no_invoice} z dnia {self.date} na kwotę {self.sum} zł.'


class InvoiceBuy(models.Model):
    class Meta:
        verbose_name = "Faktura - kupno"
        verbose_name_plural = "Faktury - kupno"
        ordering = ['-date_receipt']

    date_receipt = models.DateField("Data wpływu")
    date_issue = models.DateField("Data wystawienia")
    no_invoice = models.CharField("Nr. faktury", max_length=30)
    sum = models.DecimalField('Kwota [zł]', max_digits=10, decimal_places=2, null=True, blank=True)
    date_of_payment = models.DateField("Termin płatności")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name='invoicebuy')
    period_from = models.DateField("Okres od")
    period_to = models.DateField("Okres do")

    information = models.TextField("Informacje", blank=True, default="")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change_date = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='invoicebuy')

    def __str__(self):
        return f'Faktura nr. {self.no_invoice} z dnia {self.date_issue}'


class InvoiceItems(models.Model):
    class Meta:
        verbose_name = "Element faktury"
        verbose_name_plural = "Elementy faktury"

    invoice_id = models.ForeignKey(InvoiceBuy, on_delete=models.CASCADE, verbose_name='ID Faktury',
                                   related_name='invoiceitems')

    account = models.ForeignKey(FinanceSource, on_delete=models.CASCADE, verbose_name="Konto",
                                related_name="invoiceitems")
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="Powiat",
                               related_name='invoiceitems')
    sum = models.DecimalField("Kwota [zł]", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.account} - {self.county} - {self.sum} zł.'
