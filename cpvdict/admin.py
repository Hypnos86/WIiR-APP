from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from cpvdict.models import Typecpv


# Register your models here.
class TypecpvResource(resources.ModelResource):
    nocpv = Field(attribute='nocpv', column_name='Nr. CPV')
    name = Field(attribute='name', column_name='Nazwa')

    class Meta:
        model = Typecpv
        export_order = ('nocpv', 'name')


@admin.register(Typecpv)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['nocpv', 'name']
    search_fields = ['nocpv', 'name']
    resource_class = TypecpvResource
