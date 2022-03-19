from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from units.models import Powiat, UnitKind, Unit


# admin.site.register(Post, PostAdmin)
class PowiatResource(resources.ModelResource):
    swop_id = Field(attribute='swop_id', column_name='ID SWOP')
    powiat = Field(attribute='powiat', column_name='Powiat')

    class Meta:
        model = Powiat
        fields = ('swop_id', 'powiat')
        export_order = ('swop_id', 'powiat')


@admin.register(Powiat)
class PowiatAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['swop_id', 'powiat']
    resource_class = PowiatResource


class UnitResource(resources.ModelResource):
    powiat = Field(attribute='powiat', column_name='Powiat')
    unit_kind = Field(attribute='unit_kind', column_name='Rodzaj jednostki')
    kod_pocztowy = Field(attribute='kod_pocztowy', column_name='Kod pocztowy')
    address = Field(attribute='address', column_name='Adres')
    miasto = Field(attribute='miasto', column_name='Miasto')
    owner = Field(attribute='owner', column_name='Właściciel')

    class Meta:
        model = Unit
        fields = ('id',)
        export_order = ('id', 'powiat', 'unit_kind', 'address', 'kod_pocztowy', 'miasto', 'owner')


@admin.register(Unit)
class UnitAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['powiat', 'unit_kind', 'address', 'kod_pocztowy', 'miasto', 'owner', 'aktywna']
    search_fields = ['address', 'miasto']
    list_filter = ['powiat']
    resource_class = UnitResource


admin.site.register(UnitKind)
