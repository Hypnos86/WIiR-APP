from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from main.models import Team, OrganisationTelephone, Employer, IndustryType, AccessModule, Command, \
    SecretariatTelephone, Car, NecesseryFile

admin.site.site_title = "Admin WIiR-APP"
admin.site.index_title = "Witaj w aplikacji WIiR-APP"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'priority', 'active']


@admin.register(NecesseryFile)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_date']


@admin.register(SecretariatTelephone)
class SecretariatTelephoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'fax_number', 'secretariat_number', 'information', 'create']
    list_display_links = ('secretariat_number',)


@admin.register(IndustryType)
class IndustryTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'industry']
    list_display_links = ('industry',)


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
    list_display = ['id', 'name', 'last_name', 'team', 'industry_specialist', 'industry', 'deleted']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(AccessModule)
class AccessModuleAdmin(admin.ModelAdmin):
    list_display = ['user_name']
    ordering = ['user']
    search_fields = ['user']

    def user_name(self, obj):
        user_first_name = obj.user.first_name
        user_last_name = obj.user.last_name
        user = obj.user
        return f'{user} - {user_first_name} {user_last_name}'

    user_name.short_description = 'Użytkownicy'


class CommandResource(resources.ModelResource):
    title = Field(attribute='title', column_name='Tytuł')
    content = Field(attribute='content', column_name='Dotyczy')
    create_date = Field(attribute='create_date', column_name='Data dodania')

    class Meta:
        model = Command
        export_order = ('title', 'create_date')


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'change', 'create_date']
    list_display_links = ('title',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['rent_date', 'target', 'create_date', 'change', 'author']
    list_display_links = ('target',)
    filter_horizontal = ['borrower']
    autocomplete_fields = ['borrower']
