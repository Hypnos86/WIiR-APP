from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from contracts.models import Stan, Rodzaj, Podstawa, LegalBasicZzp, Guarantee, Period, ContractImmovables, \
    AneksImmovables, ContractAuction, AneksContractAuction

# Register your models here.
admin.site.register(Stan)
admin.site.register(Rodzaj)
admin.site.register(Podstawa)
admin.site.register(LegalBasicZzp)


@admin.register(Guarantee)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['guarantee']


@admin.register(Period)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['period']


class ContractResource(resources.ModelResource):
    data_umowy = Field(attribute='data_umowy', column_name='Data umowy')
    nrumowy = Field(attribute='nrumowy', column_name='Nr umowy')
    kontrahent = Field(attribute='kontrahent', column_name='Kontrachent')
    podstawa = Field(attribute='podstawa', column_name='Podstawa prawna')
    okres_obowiazywania = Field(attribute='okres_obowiazywania', column_name='Okres obowiązywania')
    rodzaj = Field(attribute='rodzaj', column_name='Rodzaj umowy')
    pow_uzyczona = Field(attribute='pow_uzyczona', column_name='Powieżchnia użytkowa')
    unit = Field(attribute='unit', column_name='Jednostka')
    stan = Field(attribute='stan', column_name='stan')

    class Meta:
        model = ContractImmovables
        fields = ('id',)
        export_order = ('id', 'data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj',
                        'pow_uzyczona', 'unit', 'stan')


@admin.register(ContractImmovables)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj',
                    'pow_uzyczona', 'koszt_czynsz', 'koszt_prad', 'koszt_gaz', 'koszt_woda', 'koszt_co', 'koszt_smieci',
                    'unit', 'stan', 'archives', 'create', 'change', 'author']
    search_fields = ['nrumowy', 'kontrahent']
    preserve_filters = True
    resource_class = ContractResource


@admin.register(AneksImmovables)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['contractimmovables', 'data_aneksu', 'create', 'autor']
    search_fields = ['data_aneksu', 'contract']


class ContractAuctionResource(resources.ModelResource):
    date = Field(attribute='date', column_name='Data')
    no_contract = Field(attribute='no_contract')
    contractor = Field(attribute='contractor', column_name='Wykonawca')
    price = Field(attribute='price', column_name='Wartość umowy')
    legal_basic_zzp = Field(attribute='legal_basic_zzp', column_name='Tryb UPZP')
    end_date = Field(attribute='end_date', column_name='Data realizacji')
    unit = Field(attribute='unit', column_name='Jednostka')
    last_report_date = Field(attribute='last_report_date', column_name='Data protokołu końcowego')
    guarantee = Field(attribute='guarantee', column_name='Rodzaj gwarancji')
    guarantee_period = Field(attribute='guarantee_period', column_name='Okres gwarancji')
    warranty_period = Field(attribute='warranty_period', column_name='Okres rękojmi')
    security_percentage = Field(attribute='security_percentage', column_name='Procent zabezpieczenia')
    contract_security = Field(attribute='security_percentage', column_name='Kwota zabezpieczenia')

    class Meta:
        model = ContractAuction
        fields = ('date', 'no_contract', 'contractor', 'price', 'legal_basic_zzp', 'end_date', 'unit',
                  'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percentage',
                  'contract_security',
                  )
        export_order = ('date', 'no_contract', 'contractor', 'price', 'legal_basic_zzp', 'end_date', 'unit',
                        'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percentage',
                        'contract_security')


@admin.register(ContractAuction)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_contract', 'contractor', 'price', 'legal_basic_zzp', 'end_date', 'unit',
                    'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percentage',
                    'contract_security', 'create', 'change', 'author']
    search_fields = ['no_contract', 'legal_basic_zzp', 'last_report_date', 'guarantee', 'guarantee_period',
                     'warranty_period', 'security_percentage',
                     'contract_security']
    resources_class = ContractAuctionResource


@admin.register(AneksContractAuction)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['date', 'price_change', 'price_after_change', 'create', 'author']
