from django.contrib import admin
from constructioninspections.models import TechnicalCondition, TypeInspection, BuildingInspectionOneYear, \
    ChimneyInspection

# Register your models here.
admin.site.register(TechnicalCondition)
admin.site.register(TypeInspection)


@admin.register(BuildingInspectionOneYear)
class BuildingInspectionOneYearAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]



admin.site.register(ChimneyInspection)
