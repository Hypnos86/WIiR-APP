from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from .models import Contractor


# admin.site.register(Post, PostAdmin)
class ContractorResource(resources.ModelResource):
    nocuntractor = Field(attribute='nocuntractor', column_name='Nr. kontrahenta')
    name = Field(attribute='name', column_name='Nazwa kontrahenta')
    nip = Field(attribute='nip', column_name='NIP')
    address = Field(attribute='address', column_name='Adres')
    zip_code = Field(attribute='zip_code', column_name='Kod pocztowy')
    city = Field(attribute='city', column_name='Miasto')
    information = Field(attribute='information', column_name='Informacje')

    # data_utworzenia = Field(attribute='data_utworzenia', column_name='Data utworzenia', widget=DateWidget('%d/%m/%Y'))
    # autor = Field(attribute='autor', column_name='Autor')

    class Meta:
        model = Contractor
        export_order = ('nocuntractor', 'name', 'nip', 'address', 'zip_code', 'city', 'information')


@admin.register(Contractor)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['nocuntractor', 'name', 'nip', 'address', 'zip_code', 'city', 'information', 'creation_date',
                    'author']
    search_fields = ['nocuntractor', 'name', 'nip', 'address', 'zip_code', 'city']
    resource_class = ContractorResource
