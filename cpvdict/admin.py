from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from cpvdict.models import Typecpv, OrderingObject


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


class OrderingObjectResource(resources.ModelResource):
    name_id = Field(attribute='name_id', column_name='ID')
    name = Field(attribute='name', column_name='Nazwa')
    cpv = Field(attribute='cpv', column_name='cpv')

    # usedSum = Field(attribute='nusedSum', column_name='Wykorzystano')
    # leftSum = Field(attribute='leftSum', column_name='Pozostało')

    class Meta:
        model = OrderingObject
        export_order = ('id', 'name_id', 'name', 'cpv')


@admin.register(OrderingObject)
class OrderingObjectAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name_id', 'name']
    search_fields = ['name_id', 'name']
    filter_horizontal = ['cpv']
    resource_class = OrderingObjectResource