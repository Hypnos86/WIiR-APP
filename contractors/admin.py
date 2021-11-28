from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from import_export.widgets import DateWidget

from .models import Contractor


# admin.site.register(Post, PostAdmin)
class ContractorResource(resources.ModelResource):
    nazwa = Field(attribute='nazwa', column_name='Nazwa kontrahenta')
    adres = Field(attribute='adres', column_name='Adres')
    kod_pocztowy = Field(attribute='kod_pocztowy', column_name='Kod pocztowy')
    miasto = Field(attribute='miasto', column_name='Miasto')
    informacje = Field(attribute='informacje', column_name='Informacje')
    # data_utworzenia = Field(attribute='data_utworzenia', column_name='Data utworzenia', widget=DateWidget('%d/%m/%Y'))
    # autor = Field(attribute='autor', column_name='Autor')

    class Meta:
        model = Contractor
        fields = ('id',)
        export_order = ('id', 'nazwa', 'adres', 'kod_pocztowy', 'miasto', 'informacje')


@admin.register(Contractor)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nazwa', 'adres', 'kod_pocztowy', 'miasto', 'informacje', 'data_utworzenia', 'autor']
    search_fields = ['nazwa', 'adres', 'kod_pocztowy', 'miasto']
    resource_class = ContractorResource
