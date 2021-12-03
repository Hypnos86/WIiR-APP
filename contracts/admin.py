from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from contracts.models import Contract, Stan, Rodzaj, Podstawa


# Register your models here.
class ContractResource(resources.ModelResource):
    data_umowy = Field(attribute='data_umowy', column_name='Data umowy')
    nrumowy = Field(attribute='nrumowy', column_name='Nr umowy')
    kontrahent = Field(attribute='kontrahent', column_name='Kontrachent')
    podstawa = Field(attribute='podstawa', column_name='Podstawa prawna')
    okres_obowiazywania = Field(attribute='okres_obowiazywania', column_name='Okres obowiązywania')
    rodzaj
    pow_uzyczona
    koszt_prad
    inf_prad
    koszt_gaz
    inf_gaz
    koszt_woda
    inf_woda
    koszt_co
    inf_co
    unit
    stan
    comments
    archives
    create
    change
    autor

    class Meta:
        model = Contract
        fields = ('id',)
        export_order = ('id', 'data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj',
                        'pow_uzyczona',
                        'koszt_prad', 'inf_prad', 'koszt_gaz', 'inf_gaz', 'koszt_woda', 'inf_woda', 'koszt_co',
                        'inf_co',
                        'unit', 'stan', 'comments', 'archives', 'create', 'change', 'autor')


@admin.register(ContractResource)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj',
                    'pow_uzyczona',
                    'koszt_prad', 'inf_prad', 'koszt_gaz', 'inf_gaz', 'koszt_woda', 'inf_woda', 'koszt_co', 'inf_co',
                    'unit', 'skan', 'stan', 'comments', 'archives', 'create', 'change', 'autor']
    resource_class = ContractResource


# admin.site.register(Contract)
admin.site.register(Stan)
admin.site.register(Rodzaj)
admin.site.register(Podstawa)
