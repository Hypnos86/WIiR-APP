from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from main.models import Telephone, Team, OrganisationTelephone, Employer, IndustryType, AccessModule

# Register your models here.
# admin.site.site_header ="WIiR-APP"
admin.site.site_title = "Admin WIiR-APP"
admin.site.index_title = "Witaj w aplikacji WIiR-APP"

admin.site.register(Team)
admin.site.register(IndustryType)


class TelephoneResource(resources.ModelResource):
    team = Field(attribute='team', column_name='Komórka')
    position = Field(attribute='position', column_name='Stanowisko')
    fname = Field(attribute='fname', column_name='Imię')
    lname = Field(attribute='lname', column_name='Nazwisko')
    no_room = Field(attribute='no_room', column_name='Numer pokoju')
    no_tel_room = Field(attribute='no_tel_room', column_name='Numer telefonu słóźbowego')
    no_tel_private = Field(attribute='no_tel_private', column_name='Numer komórkowy')
    information = Field(attribute='information', column_name='Informacje')

    class Meta:
        model = Telephone
        export_order = ('team', 'position', 'fname', 'lname', 'no_room', 'no_tel_room', 'no_tel_private')


@admin.register(Telephone)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['team', 'position', 'fname', 'lname', 'no_room', 'no_tel_room', 'no_tel_private', 'information']
    search_fields = ['team', 'position', 'fname', 'lname', 'no_tel_room', 'no_tel_private', 'information']
    resource_class = TelephoneResource


@admin.register(OrganisationTelephone)
class OrganisationTelephoneAdmin(admin.ModelAdmin):
    list_display = ['add_date', 'telephone_book']


class EmployerResource(resources.ModelResource):
    name = Field(attribute='name', column_name='Imię')
    last_name = Field(attribute='last_name', column_name='Nazwisko')
    team = Field(attribute='team', column_name='Zespół')
    industry_specialist = Field(attribute='industry_specialist', column_name='Branżysta')
    industry = Field(attribute='industry', column_name='Branża')

    class Meta:
        model = Employer
        export_order = ('name', 'last_name', 'team', 'industry_specialist', 'industry')


@admin.register(Employer)
class EmployerAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'team', 'industry_specialist', 'industry']


@admin.register(AccessModule)
class AccessModuleAdmin(admin.ModelAdmin):
    list_display = ['user', 'contractors_module', 'contracts_immovables_module', 'investments_module', 'invoices_module', 'cpvdict_module']
