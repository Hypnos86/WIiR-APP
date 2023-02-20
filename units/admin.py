from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from units.models import County, TypeUnit, Unit


# admin.site.register(Post, PostAdmin)
class CountyResource(resources.ModelResource):
    swop_id = Field(attribute='swop_id', column_name='ID SWOP')
    county = Field(attribute='name', column_name='Powiat')

    class Meta:
        model = County
        fields = ( 'swop_id', 'county')
        export_order = ('swop_id', 'county')


@admin.register(County)
class CountyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'swop_id', 'id_order', 'name']
    list_display_links = ('name',)
    resource_class = CountyResource


class UnitResource(resources.ModelResource):
    county = Field(attribute='county', column_name='Powiat')
    type = Field(attribute='type', column_name='Rodzaj jednostki')
    zip_code = Field(attribute='zip_code', column_name='Kod pocztowy')
    address = Field(attribute='address', column_name='Adres')
    city = Field(attribute='city', column_name='Miasto')
    manager = Field(attribute='manager', column_name='Zarządca')
    swop_id = Field(attribute='county__swop_id', column_name='SWOP ID')

    class Meta:
        model = Unit
        fields = ('swop_id', 'county', 'type', 'address', 'zip_code', 'city')
        export_order = ('swop_id', 'county', 'type', 'address', 'zip_code', 'city')


@admin.register(Unit)
class UnitAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['county', 'type', 'address', 'zip_code', 'city', 'status']
    search_fields = ['address', 'city', 'type__type_full']
    list_filter = ['county']
    list_display_links = ['address']
    resource_class = UnitResource


@admin.register(TypeUnit)
class TypeUnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_short', 'type_full']
