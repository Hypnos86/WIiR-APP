from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from contracts.models import TypeOfContract, LegalBasic, Guarantee, ContractImmovables, \
    AnnexImmovables, ContractAuction, AnnexContractAuction, GuaranteePeriod, WarrantyPeriod

# Register your models here.
admin.site.register(TypeOfContract)

admin.site.register(GuaranteePeriod)
admin.site.register(WarrantyPeriod)


@admin.register(Guarantee)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['guarantee']


class ContractImmovablesResource(resources.ModelResource):
    date = Field(attribute='date', column_name='Data umowy')
    no_contract = Field(attribute='no_contract', column_name='Nr umowy')
    contractor = Field(attribute='contractor', column_name='Kontrachent')
    legal_basic = Field(attribute='legal_basic', column_name='Podstawa prawna')
    period_of_validity = Field(attribute='period_of_validity', column_name='Okres obowiązywania')
    type_of_contract = Field(attribute='type_of_contract', column_name='Rodzaj umowy')
    usable_area = Field(attribute='usable_area', column_name='Powieżchnia użytkowa')
    unit = Field(attribute='unit', column_name='Jednostka')
    state = Field(attribute='state', column_name='Stan')

    class Meta:
        model = ContractImmovables
        fields = ('id',)
        export_order = (
            'id', 'date', 'no_contract', 'contractor', 'legal_basic', 'period_of_validity', 'type_of_contract',
            'usable_area', 'unit', 'state')


@admin.register(ContractImmovables)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_contract', 'contractor', 'legal_basic', 'period_of_validity', 'type_of_contract',
                    'usable_area', 'rent_cost', 'electric_cost', 'gas_cost', 'water_cost', 'central_heating_cost',
                    'garbage_cost', 'garbage_tax_cost', 'property_cost', 'unit', 'state', 'creation_date',
                    'change', 'author']
    search_fields = ['no_contract', 'contractor']
    list_filter = ['state']
    preserve_filters = True
    resource_class = ContractImmovablesResource


@admin.register(AnnexImmovables)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['contract_immovables', 'date_annex', 'creation_date', 'author']
    search_fields = ['date_annex', 'contract']


class ContractAuctionResource(resources.ModelResource):
    date = Field(attribute='date', column_name='Data')
    no_contract = Field(attribute='no_contract')
    contractor = Field(attribute='contractor', column_name='Wykonawca')
    price = Field(attribute='price', column_name='Wartość umowy')
    legal_basic = Field(attribute='legal_basic', column_name='Tryb UPZP')
    end_date = Field(attribute='end_date', column_name='Data realizacji')
    unit = Field(attribute='unit', column_name='Jednostka')
    last_report_date = Field(attribute='last_report_date', column_name='Data protokołu końcowego')
    guarantee = Field(attribute='guarantee', column_name='Rodzaj gwarancji')
    guarantee_period = Field(attribute='guarantee_period', column_name='Okres gwarancji')
    warranty_period = Field(attribute='warranty_period', column_name='Okres rękojmi')
    security_percent = Field(attribute='security_percent', column_name='Procent zabezpieczenia')
    security_sum = Field(attribute='security_sum', column_name='Kwota zabezpieczenia')

    class Meta:
        model = ContractAuction
        fields = ('date', 'no_contract', 'contractor', 'price', 'legal_basic', 'end_date', 'unit',
                  'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percent',
                  'security_sum',
                  )
        export_order = ('date', 'no_contract', 'contractor', 'price', 'legal_basic', 'end_date', 'unit',
                        'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percent',
                        'security_sum')


@admin.register(ContractAuction)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date', 'no_contract', 'contractor', 'price', 'work_scope', 'legal_basic', 'end_date', 'unit',
                    'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percent',
                    'security_sum', 'creation_date', 'change_date', 'author']
    search_fields = ['no_contract', 'legal_basic', 'last_report_date', 'guarantee', 'guarantee_period',
                     'warranty_period', 'security_percent',
                     'security_sum']
    filter_horizontal = ['worker']
    resources_class = ContractAuctionResource


@admin.register(AnnexContractAuction)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['date', 'price_change', 'price_after_change', 'creation_date', 'author']


class LegalBasicResource(resources.ModelResource):
    act = Field(attribute='act', column_name='Ustawa')
    legal_basic = Field(attribute='legal_basic', column_name='Paragraf')
    legal_basic_text = Field(attribute='legal_basic_text', column_name='Tekst paragrafu')

    class Meta:
        model = LegalBasic
        fields = ('act', 'legal_basic', 'legal_basic_text')
        export_order = ('act', 'legal_basic', 'legal_basic_text')


@admin.register(LegalBasic)
class LegalBasicAdmin(admin.ModelAdmin):
    list_display = ['act', 'legal_basic', 'legal_basic_text']
