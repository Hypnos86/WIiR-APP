from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ManyToManyWidget
from import_export.admin import ExportMixin
from import_export.fields import Field
from cpvdict.models import Typecpv, Genre, OrderLimit, Order, TypeOrder


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
    date = Field(attribute='date', column_name='Date')
    no_order = Field(attribute='no_order', column_name='Zlecenie')
    sum = Field(attribute='sum', column_name='Szacowana kwota')
    typeorder = Field(attribute='typeorder', column_name='Rodzaj zamówienia')
    genre = Field(attribute='genre', column_name='ID rodzajowości')
    unit = Field(attribute='unit', column_name='Jednostka')
    brakedown = Field(attribute='brakedown', column_name='Awaria')
    content = Field(attribute='content', column_name='Zakres')
    author = Field(attribute='author', column_name='Autor')

    class Meta:
        model = Order
        export_order = ('date', 'no_order', 'sum', 'typeorder', 'genre', 'unit', 'brakedown', 'content', 'author')


@admin.register(Order)
class OrderAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_order', 'sum', 'typeorder', 'genre', 'brakedown', 'content']
    search_fields = ['no_cpv', 'name']
    resource_class = OrderResource


@admin.register(OrderLimit)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['limit']


@admin.register(TypeOrder)
class TypeOrderAdmin(admin.ModelAdmin):
    list_display = ['type']
