from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from fixedasset.models import KindBuilding, Building

admin.site.register(KindBuilding)


class BuildingResource(resources.ModelResource):
    county = Field(attribute='unit__county__name', column_name='Powiat')
    no_inventory = Field(attribute='no_inventory', column_name='Nr. ewidencyjny')
    unit = Field(attribute='unit', column_name="Jednostka")
    building_name = Field(attribute='building_name', column_name='Nazwa budynku')
    kind = Field(attribute='kind', column_name='Rodzaj budynku')
    state = Field(attribute='state', column_name='aktywny')

    class Meta:
        model = Building
        fields = ['county', 'unit', 'no_inventory', 'kind', 'building_name', 'state']
        export_order = ('county', 'unit', 'no_inventory', 'kind', 'building_name', 'state')


@admin.register(Building)
class TypeUnitAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['no_inventory', 'unit', 'building_name', 'kind', 'state', 'author']
    search_fields = ['no_inventory', 'building_name', 'unit__county__name']
    list_display_links = ['no_inventory']
    autocomplete_fields = ['unit']
    resource_class = BuildingResource
