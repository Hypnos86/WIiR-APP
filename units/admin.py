from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from units.models import Powiat, Rodzaj, Unit


# admin.site.register(Post, PostAdmin)
class PowiatResource(resources.ModelResource):
    swop_id = Field(attribute='swop_id', column_name='ID SWOP')
    powiat = Field(attribute='powiat', column_name='Powiat')

    class Meta:
        model = Powiat
        fields = ('swop_id', 'powiat')
        export_order = ('swop_id', 'powiat')


class UnitResource(resources.ModelResource):
    powiat = Field(attribute='powiat', column_name='Powiat')
    rodzaj = Field(attribute='rodzaj', column_name='Rodzaj jednostki')
    kod_pocztowy = Field(attribute='kod_pocztowy', column_name='Kod pocztowy')
    adres = Field(attribute='adres', column_name='Adres')
    miasto = Field(attribute='miasto', column_name='Miasto')

    class Meta:
        model = Unit
        fields = ('id',)
        export_order = ('id', 'powiat', 'rodzaj', 'adres', 'kod_pocztowy', 'miasto')


@admin.register(Powiat)
class PowiatAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'swop_id', 'powiat']
    resource_class = PowiatResource


admin.site.register(Rodzaj)


@admin.register(Unit)
class JednotskaAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'powiat', 'rodzaj', 'adres', 'kod_pocztowy', 'miasto', 'aktywna']
    search_fields = ['adres, miasto']
    list_filter = ['powiat']
    resource_class = UnitResource
