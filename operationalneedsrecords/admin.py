from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportMixin
from operationalneedsrecords.models import RegistrationType, MeritsType, NeedsLetter


class NeedsLetterResource(resources.ModelResource):
    receipt_date = Field(attribute="receipt_date", column_name="Data wpływu")
    case_sign = Field(attribute="case_sign", column_name="Znak pisma")
    unit = Field(attribute="unit", column_name="Jednostka")
    case_description = Field(attribute="case_description", column_name="Opis sprawy")
    registration_type = Field(attribute="registration_type", column_name="Rodzaj zgłoszenia")
    no_secretariats_diary = Field(attribute="no_secretariats_diary", column_name="Nr. z dziennika")
    receipt_date_to_team = Field(attribute="receipt_date_to_team", column_name="Data wpływu do Zespołu")
    case_sign_team = Field(attribute="case_sign_team", column_name="Znak sprawy WiiR")
    cost = Field(attribute="cost", column_name="Koszt realizacji")
    isDone = Field(attribute="isDone", column_name="Zrealizowane")
    information = Field(attribute="information", column_name="Informacje")

    class Meta:
        models = NeedsLetter
        fields = ('receipt_date', 'case_sign', 'unit', 'case_description', 'registration_type', 'no_secretariats_diary',
                  'receipt_date_to_team', 'case_sign_team', 'cost', 'isDone', 'information')
        export_order = (
        'receipt_date', 'case_sign', 'unit', 'case_description', 'registration_type', 'no_secretariats_diary',
        'receipt_date_to_team', 'case_sign_team', 'cost', 'isDone', 'information')


@admin.register(NeedsLetter)
class NeedLetterAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['receipt_date', 'case_sign', 'unit', 'registration_type', 'receipt_date_to_team', 'case_sign_team',
                    'isDone', 'author', 'creation_date', 'change']
    search_fields = ['case_sign', 'unit', 'registration_type', 'receipt_date_to_team', 'case_sign_team']
    list_display_links = ['unit']

