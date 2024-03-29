from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportMixin
from invoices.models import InvoiceSell, InvoiceBuy, InvoiceItems, DocumentTypes, CorrectiveNote


# Register your models here.
class InvoiceSellResource(resources.ModelResource):
    date = Field(attribute='date', column_name='Data wystawienia')
    no_invoice = Field(attribute='no_invoice', column_name='Nr. faktury')
    contractor = Field(attribute='contractor', column_name='Kontrahent')
    sum = Field(attribute='sum', column_name='Kwota')
    county = Field(attribute='county', column_name='Powiat')
    period_from = Field(attribute='period_from', column_name='Okres od')
    period_to = Field(attribute='period_to', column_name='Okres do')
    creation_date = Field(attribute='creator', column_name='Osoba wystawiająca')
    information = Field(attribute='comments', column_name='Informacje')

    class Meta:
        model = InvoiceSell
        fields = (
            'date', 'no_invoice', 'contractor', 'sum', 'county', 'period_from', 'period_to', 'creator', 'information')
        export_order = ('date', 'no_invoice', 'sum', 'period_from', 'period_to', 'county', 'creator', 'information')


@admin.register(InvoiceSell)
class InvoiceSellAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_invoice', 'contractor', 'sum', 'period_from', 'period_to', 'county',
                    'creator', 'author']
    search_fields = ['no_invoice', 'contractor', 'county']
    list_display_links = ['no_invoice']
    preserve_filters = True
    resource_class = InvoiceSellResource


class CorrectiveNoteResource(resources.ModelResource):
    date = Field(attribute='date', column_name='Data wystawienia')
    no_note = Field(attribute='no_note', column_name='Nr. noty')
    contractor = Field(attribute='contractor', column_name='Kontrahent')
    corrective_invoice = Field(attribute='corrective_invoice', column_name='Korygowana faktura')
    information = Field(attribute='information', column_name='Korygowana treść')

    class Meta:
        model = CorrectiveNote
        fields = ('date', 'no_note', 'contractor', 'corrective_invoice', 'information')


@admin.register(CorrectiveNote)
class CorrectiveNoteAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_note', 'contractor', 'corrective_invoice']
    search_fields = ['no_note', 'corrective_invoice']
    search_help_text = "Mozliwość szukania: nr. noty, korygowana faktura"
    list_display_links = ['no_note']
    resource_class = CorrectiveNoteResource


@admin.register(DocumentTypes)
class DocumentTypesAdmin(admin.ModelAdmin):
    list_display = ['id','type']


@admin.register(InvoiceItems)
class InvoiceItemsAdmin(admin.ModelAdmin):
    ordering = ['invoice_id', 'account', 'county', 'sum']
    list_display = ['invoice_id', 'id', 'account', 'county', 'sum']
    search_fields = ["invoice_id__no_invoice", "county__name", "account__section__section"]
    list_filter = ['county']


@admin.register(InvoiceBuy)
class InvoiceBuyAdmin(admin.ModelAdmin):
    list_display = ['date_receipt', 'date_issue', 'no_invoice', 'sum', 'contractor', 'creation_date',
                    'author']
    list_display_links = ['no_invoice']
    search_fields = ['no_invoice', 'contractor__name', 'contractor__nip']
    search_help_text = "Możliwość szukania: nr. faktury, nazwa kontrahenta, NIP"
