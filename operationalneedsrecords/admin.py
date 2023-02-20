from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from operationalneedsrecords.models import RegistrationType, MetricsCaseType, NeedsLetter


class NeedsLetterResource(resources.ModelResource):
    receipt_date = Field(attribute="receipt_date", column_name="Data wpływu")
    case_sign = Field(attribute="case_sign", column_name="Znak pisma")
    county = Field(attribute="unit__county__name", column_name="Powiat")
    typeOfUnit = Field(attribute="unit__type__type_short", column_name="Rodzaj jednostki")
    unit = Field(attribute="unit", column_name="Jednostka")
    case_description = Field(attribute="case_description", column_name="Opis sprawy")
    case_type = Field(attribute="case_type", column_name="Rodzaj sprawy")
    registration_type = Field(attribute="registration_type", column_name="Rodzaj zgłoszenia")
    no_secretariats_diary = Field(attribute="no_secretariats_diary", column_name="Nr. z dziennika")
    receipt_date_to_team = Field(attribute="receipt_date_to_team", column_name="Data wpływu do Zespołu")
    case_sign_team = Field(attribute="case_sign_team", column_name="Znak sprawy WiiR")
    employer = Field(attribute="employer", column_name="Branżysta")
    cost = Field(attribute="cost", column_name="Koszt realizacji")
    isDone = Field(attribute="isDone", column_name="Zrealizowane")
    information = Field(attribute="information", column_name="Informacje")

    class Meta:
        models = NeedsLetter
        fields = ('id',)
        export_order = (
            'receipt_date', 'no_secretariats_diary', 'receipt_date_to_team', 'case_sign', 'county', 'typeOfUnit',
            'unit', 'case_description', 'case_type', 'registration_type', 'case_sign_team', 'cost', 'isDone',
            'information')


@admin.register(NeedsLetter)
class NeedLetterAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['receipt_date', 'case_sign', 'unit', 'case_type', 'registration_type', 'isDone', 'employer',
                    'author', 'creation_date']
    search_fields = ['case_sign', 'unit__city', 'registration_type__registration_type', 'case_sign_team']
    list_display_links = ['unit']
    list_filter = ('isDone', 'unit__county__name')
    resource_class = NeedsLetterResource


@admin.register(RegistrationType)
class RegistrationTypeAdmin(admin.ModelAdmin):
    list_display = ['registration_type']


@admin.register(MetricsCaseType)
class MetricsCaseTypeAdmin(admin.ModelAdmin):
    list_display = ['metric_type']
