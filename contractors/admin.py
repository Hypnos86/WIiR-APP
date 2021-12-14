from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from .models import Contractorsell


# admin.site.register(Post, PostAdmin)
class ContractorResource(resources.ModelResource):
    nocuntractor = Field(attribute='nocuntractor', column_name='Nr. kontrahenta')
    nazwa = Field(attribute='nazwa', column_name='Nazwa kontrahenta')
    nip = Field(attribute='nip', column_name='NIP')
    adres = Field(attribute='adres', column_name='Adres')
    kod_pocztowy = Field(attribute='kod_pocztowy', column_name='Kod pocztowy')
    miasto = Field(attribute='miasto', column_name='Miasto')
    informacje = Field(attribute='informacje', column_name='Informacje')

    # data_utworzenia = Field(attribute='data_utworzenia', column_name='Data utworzenia', widget=DateWidget('%d/%m/%Y'))
    # autor = Field(attribute='autor', column_name='Autor')

    class Meta:
        model = Contractorsell
        export_order = ('nocuntractor', 'nazwa', 'nip', 'adres', 'kod_pocztowy', 'miasto', 'informacje')


@admin.register(Contractorsell)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['nocuntractor', 'nazwa', 'nip', 'adres', 'kod_pocztowy', 'miasto', 'informacje', 'data_utworzenia',
                    'autor']
    search_fields = ['nocuntractor', 'nazwa', 'nip', 'adres', 'kod_pocztowy', 'miasto']
    resource_class = ContractorResource
