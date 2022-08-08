from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ManyToManyWidget
from import_export.admin import ExportMixin
from import_export.fields import Field
from cpvdict.models import Typecpv, Genre, OrderLimit, Order, TypeOrder, Tax
from units.models import Unit


# Register your models here.
class TypecpvResource(resources.ModelResource):
    no_cpv = Field(attribute='no_cpv', column_name='Nr. CPV')
    name = Field(attribute='name', column_name='Nazwa')

    class Meta:
        model = Typecpv
        export_order = ('no_cpv', 'name')


@admin.register(Typecpv)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['no_cpv', 'name']
    search_fields = ['no_cpv', 'name']
    resource_class = TypecpvResource


class GenreResource(resources.ModelResource):
    name_id = Field(attribute='name_id', column_name='ID')
    name = Field(attribute='name', column_name='Nazwa')
    cpv = fields.Field(attribute='cpv', column_name='Nr cpv', widget=ManyToManyWidget(Genre, ', ', field='no_cpv'))

    class Meta:
        model = Genre
        fields = ['id', 'name_id', 'name', 'cpv']
        export_order = ('id', 'name_id', 'name', 'cpv')


@admin.register(Genre)
class OrderingObjectAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name_id', 'name']
    search_fields = ['name_id', 'name']
    filter_horizontal = ['cpv']
    resource_class = GenreResource


class OrderResource(resources.ModelResource):
    date = Field(attribute='date', column_name='Data')
    no_order = Field(attribute='no_order', column_name='Zlecenie')
    sum_netto = Field(attribute='sum_netto', column_name='Kwota netto')
    vat = Field(attribute='vat', column_name='vat')
    sum_brutto = Field(attribute='sum_brutto', column_name='Kwota brutto')
    typeorder = Field(attribute='typeorder', column_name='Rodzaj zamówienia')
    genre = Field(attribute='genre', column_name='ID rodzajowości')
    # TODO dodać signal i zmienic model - dodatkowe pole do nazwy jednostki
    unit = fields.Field(attribute='unit', column_name='Jednostka', widget=ManyToManyWidget(Unit, ', ', field='full_name'))
    brakedown = Field(attribute='brakedown', column_name='Awaria')
    content = Field(attribute='content', column_name='Zakres')
    worker = Field(attribute='worker', column_name='Branżysta')

    class Meta:
        model = Order
        fields = ['date', 'no_order', 'sum_netto', 'vat', 'sum_brutto', 'typeorder', 'genre', 'unit', 'brakedown',
                  'content',
                  'worker']
        export_order = ('date', 'no_order', 'sum_netto', 'vat', 'sum_brutto', 'typeorder', 'genre', 'unit', 'brakedown', 'content', 'worker')


@admin.register(Order)
class OrderAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_order', 'sum_netto', 'sum_brutto', 'typeorder', 'genre', 'brakedown']
    search_fields = ['no_order', 'no_cpv', 'name', 'typeorder__type']
    list_display_links = ('no_order',)
    resource_class = OrderResource


@admin.register(OrderLimit)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['year', 'euro_exchange_rate', 'limit_euro', 'limit_netto']


@admin.register(TypeOrder)
class TypeOrderAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['id', 'vat']
    list_display_links = ('vat',)
