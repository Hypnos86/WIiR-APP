from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportMixin
from invoices.models import Invoicesell, Creator


# Register your models here.
class InvoicesellResource(resources.ModelResource):
    data = Field(attribute='data', column_name='Data wystawienia')
    noinvoice = Field(attribute='noinvoice', column_name='Nr. faktury')

    contractor = Field(attribute='contractor', column_name='Kontrahent')
    sum = Field(attribute='sum', column_name='Kwota')
    contract = Field(attribute='contract', column_name='Umowa')
    period_from = Field(attribute='period_from', column_name='Okres od')
    period_to = Field(attribute='period_to', column_name='Okres do')
    creator = Field(attribute='creator', column_name='Osoba wystawiająca')
    comments = Field(attribute='comments', column_name='Informacje')

    class Meta:
        model = Invoicesell
        fields = (
            'data', 'noinvoice', 'contractor', 'sum', 'contract', 'period_from', 'period_to', 'creator', 'comments')
        export_order = ('data', 'noinvoice', 'sum', 'contractor', 'period_from', 'period_to', 'creator', 'comments')


@admin.register(Invoicesell)
class InvoicesellAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['data', 'noinvoice', 'contractor', 'sum', 'contract', 'period_from', 'period_to',
                    'creator', 'comments']
    search_fields = ['noinvoice', 'contractor']
    preserve_filters = True
    resource_class = InvoicesellResource


admin.site.register(Creator)
