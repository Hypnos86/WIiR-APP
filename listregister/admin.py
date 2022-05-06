from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from listregister.models import OfficialFlat


# Register your models here.


class OfficialFlatResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Identyfikator')
    address = Field(attribute='address', column_name='Adres')
    area = Field(attribute='area', column_name='Powierzchnia')
    room_numbers = Field(attribute='room_numbers', column_name='Ilość pokoi')
    flor = Field(attribute='flor', column_name='Piętro')
    information = Field(attribute='information', column_name='Infomracje')
    state = Field(attribute='state', column_name='Stan')

    class Meta:
        model = OfficialFlat
        fields = ('id', 'address', 'area', 'room_numbers', 'flor', 'information', 'state')
        export_order = ('id', 'address', 'area', 'room_numbers', 'flor', 'information', 'state')


@admin.register(OfficialFlat)
class CountyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['address', 'area', 'room_numbers', 'flor', 'information', 'state', 'creation_date', 'change', 'author']
    search_fields = ['address', 'area', 'room_numbers', 'flor', 'information']
    list_filter = ['state', 'flor', 'room_numbers']
    resource_class = OfficialFlatResource
