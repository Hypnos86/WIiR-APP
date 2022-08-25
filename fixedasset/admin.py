from django.contrib import admin

from fixedasset.models import KindBuilding, Building

# Register your models here.
admin.site.register(KindBuilding)


@admin.register(Building)
class TypeUnitAdmin(admin.ModelAdmin):
    list_display = ["unit", "no_inventory", "building_name", "kind", "state", "creation_date", "change", "author"]
    search_fields = ["no_inventory", "building_name", "unit__county__name"]
    list_display_links = ["no_inventory"]
    autocomplete_fields = ["unit"]
