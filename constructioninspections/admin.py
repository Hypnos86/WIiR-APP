from django.contrib import admin
from constructioninspections.models import TechnicalCondition, TypeInspection, BuildingInspectionOneYear, \
    BuildingInspectionFiveYear, ChimneyInspection, ElectricalInspectionOneYear, FireInspection, HeatingBoilerInspection, \
    AirConditionerInspection, ElectricalInspectionFiveYear

# Register your models here.
admin.site.register(TechnicalCondition)


@admin.register(TypeInspection)
class TypeInspectionAdmin(admin.ModelAdmin):
    list_display = ["id", "inspection_name"]
    list_display_links = ["inspection_name"]


@admin.register(BuildingInspectionOneYear)
class BuildingInspectionOneYearAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "date_next_inspection", "no_inventory", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(BuildingInspectionFiveYear)
class BuildingInspectionFiveYearAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(ChimneyInspection)
class ChimneyInspectionAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(ElectricalInspectionOneYear)
class ElectricalInspectionOneYearAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(ElectricalInspectionFiveYear)
class ElectricalInspectionFiveYearAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(FireInspection)
class FireInspectionAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(HeatingBoilerInspection)
class HeatingBoilerInspectionAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]


@admin.register(AirConditionerInspection)
class AirConditionerInspectionAdmin(admin.ModelAdmin):
    list_display = ["date_protocol", "no_inventory", "date_next_inspection", "author", "creation_date", "change"]
    list_display_links = ["no_inventory"]
    search_fields = ["no_inventory__no_inventory", "no_inventory__building_name", "no_inventory__kind__kind",
                     "no_inventory__unit__county__name", "no_inventory__unit__full_name"]
    list_filter = ["date_protocol", "no_inventory__unit__county__name"]
    search_help_text = "Szukaj za pomocą: Nr. inwentarzaowego, nazwy budynku, typu budynku, powiatu, nazwy jednostki wraz z adresem"
    autocomplete_fields = ["no_inventory"]
