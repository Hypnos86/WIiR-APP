from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from contracts.models import Contractimmovables, Stan, Rodzaj, Podstawa, Aneks


# Register your models here.
class ContractResource(resources.ModelResource):
    data_umowy = Field(attribute='data_umowy', column_name='Data umowy')
    nrumowy = Field(attribute='nrumowy', column_name='Nr umowy')
    kontrahent = Field(attribute='kontrahent', column_name='Kontrachent')
    podstawa = Field(attribute='podstawa', column_name='Podstawa prawna')
    okres_obowiazywania = Field(attribute='okres_obowiazywania', column_name='Okres obowiązywania')
    rodzaj = Field(attribute='rodzaj', column_name='Rodzaj umowy')
    pow_uzyczona = Field(attribute='pow_uzyczona', column_name='Powieżchnia użytkowa')
    # koszt_prad = Field(attribute='pow_uzyczona', column_name='')
    # koszt_gaz = Field(attribute='koszt_gaz', column_name='')
    # koszt_woda = Field(attribute='koszt_woda', column_name='')
    # koszt_co = Field(attribute='koszt_co', column_name='')
    unit = Field(attribute='unit', column_name='Jednostka')
    stan = Field(attribute='stan', column_name='stan')

    # comments = Field(attribute='comments', column_name='')
    # archives = Field(attribute='archives', column_name='')

    class Meta:
        model = Contractimmovables
        fields = ('id',)
        export_order = ('id', 'data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj',
                        'pow_uzyczona', 'unit', 'stan')


@admin.register(Contractimmovables)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj',
                    'pow_uzyczona', 'koszt_czynsz', 'koszt_prad', 'koszt_gaz', 'koszt_woda', 'koszt_co', 'koszt_smieci',
                    'unit', 'stan', 'archives', 'create', 'change', 'autor']
    search_fields = ['nrumowy', 'kontrahent']
    preserve_filters = True
    resource_class = ContractResource


# admin.site.register(Contract)
admin.site.register(Stan)
admin.site.register(Rodzaj)
admin.site.register(Podstawa)


@admin.register(Aneks)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['contract', 'data_aneksu', 'create', 'autor']
    search_fields = ['data_aneksu', 'contract']
