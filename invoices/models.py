from django.db import models
from enum import Enum
from contractors.models import Contractor
from units.models import County
from main.models import Employer
from sourcefinancing.models import FinanceSource
import datetime


class DocumentsTypeEnum(Enum):
    FAKTURA = "Faktura"
    KOREKTA = "Korekta"
    NOTA_KORYGUJACA = "Nota korygująca"


class DocumentTypes(models.Model):
    class Meta:
        verbose_name = "Rodzaj dokumentu księgowego"
        verbose_name_plural = "F.05 - Rodzaje dokumentów księgowych"

    type = models.CharField("Typ dokumentu", max_length=20)

    def __str__(self):
        return f"{self.type}"


class InvoiceSell(models.Model):
    class Meta:
        verbose_name = "Faktura sprzedaży"
        verbose_name_plural = "F.01 - Faktury - sprzedaż"
        ordering = ["-date"]

    relatedName = "invoicesell"

    date = models.DateField("Data wystawienia")
    no_invoice = models.CharField("Nr. faktury", max_length=11)
    doc_types = models.ForeignKey(DocumentTypes, null=False, blank=False, on_delete=models.CASCADE,
                                  verbose_name="Rodzaj dokumentu", related_name=relatedName)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name=relatedName)
    sum = models.DecimalField("Kwota [zł]", max_digits=10, decimal_places=2, null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="Powiat", related_name=relatedName)
    date_of_payment = models.DateField("Termin płatności")
    period_from = models.DateField("Okres od")
    period_to = models.DateField("Okres do")
    creator = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name="Osoba wystawiająca",
                                related_name=relatedName)
    information = models.TextField("Informacje", blank=True, default="")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change_date = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName, verbose_name="Autor")

    def __str__(self):
        return f"Faktura nr {self.no_invoice} z dnia {self.date} na kwotę {self.sum} zł."


class InvoiceBuy(models.Model):
    class Meta:
        verbose_name = "Faktura - kupno"
        verbose_name_plural = "F.03 - Faktury - kupno"
        ordering = ["-date_receipt"]

    relatedName = "invoicebuy"

    date_receipt = models.DateField("Data wpływu")
    date_issue = models.DateField("Data wystawienia")
    no_invoice = models.CharField("Nr. faktury", max_length=30)
    doc_types = models.ForeignKey(DocumentTypes, null=False, blank=False, on_delete=models.CASCADE,
                                  verbose_name="Rodzaj dokumentu",
                                  related_name=relatedName)
    sum = models.DecimalField("Kwota [zł]", max_digits=10, decimal_places=2, null=True, blank=True)
    date_of_payment = models.DateField("Termin płatności")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name=relatedName)
    information = models.TextField("Informacje", blank=True, default="")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change_date = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name=relatedName)

    def __str__(self):
        return f"{self.no_invoice} z dnia {self.date_issue.strftime('%d.%m.%Y')} r."


class InvoiceItems(models.Model):
    class Meta:
        verbose_name = "Element faktury"
        verbose_name_plural = "F.04 - Elementy faktury"
        ordering = ["invoice_id"]

    relatedName = "invoice_items"

    invoice_id = models.ForeignKey(InvoiceBuy, on_delete=models.CASCADE, verbose_name="Faktura",
                                   related_name=relatedName)
    account = models.ForeignKey(FinanceSource, on_delete=models.CASCADE, verbose_name="Konto",
                                related_name=relatedName)
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="Powiat",
                               related_name=relatedName)
    sum = models.DecimalField("Kwota brutto [zł]", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.account} - {self.county} - {self.sum} zł."


class CorrectiveNote(models.Model):
    class Meta:
        verbose_name = "Nota korygująca"
        verbose_name_plural = "F.02 - Noty korygujące"
        ordering = ["-date"]

    relatedName = "correctivenote"

    date = models.DateField("Data wystawienia")
    no_note = models.CharField("Nr. noty", max_length=15)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name=relatedName)
    corrective_invoice = models.CharField("Korygowana faktura", max_length=70)
    information = models.TextField("Korygowana treść", blank=True, default="")
    creation_date = models.DateField("Data uworzenia", auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor",
                               related_name=relatedName)

    def __str__(self):
        return f"{self.no_note} z dnia {self.date}"
