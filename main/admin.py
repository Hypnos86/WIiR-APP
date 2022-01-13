from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from main.models import Telephone, Team, OrganisationTelephone, IndustryType, Inspector

# Register your models here.
# admin.site.site_header ="WIiR-APP"
admin.site.site_title = "Admin WIiR-APP"
admin.site.index_title = "Witaj w aplikacji WIiR-APP"

admin.site.register(Team)


class TelephoneResource(resources.ModelResource):
    team = Field(attribute='team', column_name='Komórka')
    position = Field(attribute='position', column_name='Stanowisko')
    fname = Field(attribute='fname', column_name='Imię')
    lname = Field(attribute='lname', column_name='Nazwisko')
    numbroom = Field(attribute='numbroom', column_name='Numer pokoju')
    numbtelbus = Field(attribute='numbtelbus', column_name='Numer telefonu słuzbowego')
    numbtelpri = Field(attribute='numbtelpri', column_name='Numer komórkowy')
    information = Field(attribute='information', column_name='Informacje')

    class Meta:
        model = Telephone
        export_order = ('team', 'position', 'fname', 'lname', 'numbroom', 'numbtelbus', 'numbtelpri')


@admin.register(Telephone)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['team', 'position', 'fname', 'lname', 'numbroom', 'numbtelbus', 'numbtelpri', 'information']
    search_fields = ['team', 'position', 'fname', 'lname', 'numbtelbus', 'numbtelpri', 'information']
    resource_class = TelephoneResource


@admin.register(OrganisationTelephone)
class OrganisationTelephoneAdmin(admin.ModelAdmin):
    list_display = ['add_date', 'telephone_book']


@admin.register(IndustryType)
class OrganisationTelephoneAdmin(admin.ModelAdmin):
    list_display = ['industry']


@admin.register(Inspector)
class OrganisationTelephoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'industry']
