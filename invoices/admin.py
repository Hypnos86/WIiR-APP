from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportMixin
from invoices.models import InvoiceSell, InvoiceBuy, InvoiceItems, Creator


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
                    'creator', 'information', 'author']
    search_fields = ['no_invoice', 'contractor', 'county']
    preserve_filters = True
    resource_class = InvoiceSellResource


admin.site.register(Creator)


@admin.register(InvoiceItems)
class InvoiceItemsAdmin(admin.ModelAdmin):
    ordering = ['account', 'county', 'sum']
    list_display = ['account', 'county', 'sum']


@admin.register(InvoiceBuy)
class InvoiceBuyAdmin(admin.ModelAdmin):
    list_display = ['date_issue', 'date_receipt', 'no_invoice', 'contractor', 'invoice_items', 'creation_date',
                    'author']
