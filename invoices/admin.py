from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportMixin
from invoices.models import Invoicesell, Invoicebuy, Invoiceitems, Creator


# Register your models here.
class InvoicesellResource(resources.ModelResource):
    data = Field(attribute='data', column_name='Data wystawienia')
    noinvoice = Field(attribute='noinvoice', column_name='Nr. faktury')
    contractor = Field(attribute='contractor', column_name='Kontrahent')
    sum = Field(attribute='sum', column_name='Kwota')
    powiat = Field(attribute='powiat', column_name='Powiat')
    period_from = Field(attribute='period_from', column_name='Okres od')
    period_to = Field(attribute='period_to', column_name='Okres do')
    creator = Field(attribute='creator', column_name='Osoba wystawiająca')
    comments = Field(attribute='comments', column_name='Informacje')

    class Meta:
        model = Invoicesell
        fields = (
            'data', 'noinvoice', 'contractor', 'sum', 'powiat', 'period_from', 'period_to', 'creator', 'comments')
        export_order = ('data', 'noinvoice', 'sum', 'period_from', 'period_to', 'powiat', 'creator', 'comments')


@admin.register(Invoicesell)
class InvoicesellAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['data', 'noinvoice', 'contractor', 'sum', 'period_from', 'period_to', 'powiat',
                    'creator', 'comments']
    search_fields = ['noinvoice', 'contractor', 'powiat']
    preserve_filters = True
    resource_class = InvoicesellResource


admin.site.register(Creator)

@admin.register(Invoiceitems)
class InvoiceitemsAdmin(admin.ModelAdmin):
    ordering = ['acount', 'powiat', 'sum']
    list_display = ['acount', 'powiat', 'sum']


@admin.register(Invoicebuy)
class InvoicebuyAdmin(admin.ModelAdmin):
    list_display = ['datawyplytu', 'data', 'noinvoice', 'contractor', 'invoiceitems', 'create', 'autor']
