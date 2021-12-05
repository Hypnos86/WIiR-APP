from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from main.models import Telephone, Team

# Register your models here.
admin.site.register(Team)


class TelephoneResource(resources.ModelResource):
    team = Field(attribute='team', column_name='Komórka')
    position = Field(attribute='position', column_name='Stanowisko')
    fname = Field(attribute='fname', column_name='Imię')
    lname = Field(attribute='lname', column_name='Nazwisko')
    numbroom = Field(attribute='numbroom', column_name='Numer pokoju')
    numbtelbus = Field(attribute='numbtelbus', column_name='Numer telefonu słuzbowego')
    numbtelpri = Field(attribute='numbtelpri', column_name='Numer komórkowy')

    class Meta:
        model = Telephone
        fields = ('id',)
        export_order = ('id', 'team', 'position', 'fname', 'lname', 'numbroom', 'numbtelbus', 'numbtelpri')


@admin.register(Telephone)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'team', 'position', 'fname', 'lname', 'numbroom', 'numbtelbus', 'numbtelpri']
    search_fields = ['team', 'position', 'fname', 'lname', 'numbtelbus', 'numbtelpri']
    resource_class = TelephoneResource
