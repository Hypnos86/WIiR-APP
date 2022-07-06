from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from .models import Contractor


# admin.site.register(Post, PostAdmin)
class ContractorResource(resources.ModelResource):
    no_contractor = Field(attribute='no_contractor', column_name='Nr. kontrahenta')
    name = Field(attribute='name', column_name='Nazwa kontrahenta')
    nip = Field(attribute='nip', column_name='NIP')
    address = Field(attribute='address', column_name='Adres')
    zip_code = Field(attribute='zip_code', column_name='Kod pocztowy')
    city = Field(attribute='city', column_name='Miasto')
    information = Field(attribute='information', column_name='Informacje')

    class Meta:
        model = Contractor
        export_order = ('no_contractor', 'name', 'nip', 'address', 'zip_code', 'city', 'information')


@admin.register(Contractor)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['no_contractor', 'name', 'nip', 'address', 'zip_code', 'city', 'creation_date',
                    'author']
    search_fields = ['no_contractor', 'name', 'nip', 'address', 'zip_code', 'city']
    list_display_links = ('name',)
    resource_class = ContractorResource
