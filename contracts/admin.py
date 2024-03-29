from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget
from contracts.models import TypeOfContract, LegalBasic, Guarantee, ContractImmovables, \
    AnnexImmovables, ContractAuction, AnnexContractAuction, MediaType, ContractMedia, \
    GuaranteeSettlement, AnnexContractMedia, UnitMeasure, FinancialDocument
from units.models import Unit

# Register your models here.
admin.site.register(TypeOfContract)


@admin.register(GuaranteeSettlement)
class GuaranteeSettlementAdmin(admin.ModelAdmin):
    list_display = ["contract", "deadline_settlement", "settlement_sum", "script", "affirmation_settlement"]
    list_display_links = ["contract"]
    search_fields = ["contract__no_contract", "script"]


@admin.register(UnitMeasure)
class UnitMeasureAdmin(admin.ModelAdmin):
    list_display = ["id", "measureName"]
    list_display_links = ["measureName"]


@admin.register(Guarantee)
class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ["id", "guarantee"]
    list_display_links = ["guarantee"]


class ContractImmovablesResource(resources.ModelResource):
    date = Field(attribute="date", column_name="Data umowy")
    no_contract = Field(attribute="no_contract", column_name="Nr umowy")
    contractor = Field(attribute="contractor", column_name="Kontrachent")
    legal_basic = Field(attribute="legal_basic", column_name="Podstawa prawna")
    period_of_validity = Field(attribute="period_of_validity", column_name="Okres obowiązywania")
    type_of_contract = Field(attribute="type_of_contract", column_name="Rodzaj umowy")
    usable_area = Field(attribute="usable_area", column_name="Powieżchnia użytkowa")
    unit = Field(attribute="unit", column_name="Jednostka")
    state = Field(attribute="state", column_name="Stan")

    class Meta:
        model = ContractImmovables
        fields = ("id",)
        export_order = (
            "id", "date", "no_contract", "contractor", "legal_basic", "period_of_validity", "type_of_contract",
            "usable_area", "unit", "state")


@admin.register(ContractImmovables)
class ContractAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["date", "no_contract", "contractor", "period_of_validity", "type_of_contract", "unit", "state",
                    "author"]
    search_fields = ["contractor__name", "contractor__no_contractor", "no_contract", "unit__county__name",
                     "unit__city", "unit__type__type_short", "type_of_contract__type"]
    autocomplete_fields = ['contractor']
    list_filter = ["state"]
    preserve_filters = True
    resource_class = ContractImmovablesResource


@admin.register(AnnexImmovables)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["contract_immovables", "date_annex", "author"]
    search_fields = ["date_annex", "contract"]


class ContractAuctionResource(resources.ModelResource):
    date = Field(attribute="date", column_name="Data")
    no_contract = Field(attribute="no_contract")
    contractor = Field(attribute="contractor", column_name="Wykonawca")
    price = Field(attribute="price", column_name="Wartość umowy")
    legal_basic = Field(attribute="legal_basic", column_name="Tryb UPZP")
    end_date = Field(attribute="end_date", column_name="Data realizacji")
    unit = Field(attribute="unit", column_name="Jednostka")
    last_report_date = Field(attribute="last_report_date", column_name="Data protokołu końcowego")
    guarantee = Field(attribute="guarantee", column_name="Rodzaj gwarancji")
    guarantee_period = Field(attribute="guarantee_period", column_name="Okres gwarancji")
    warranty_period = Field(attribute="warranty_period", column_name="Okres rękojmi")
    security_percent = Field(attribute="security_percent", column_name="Procent zabezpieczenia")
    security_sum = Field(attribute="security_sum", column_name="Kwota zabezpieczenia")

    class Meta:
        model = ContractAuction
        fields = ("date", "no_contract", "contractor", "price", "legal_basic", "end_date", "unit",
                  "last_report_date", "guarantee", "guarantee_period", "warranty_period", "security_percent",
                  "security_sum",
                  )
        export_order = ("date", "no_contract", "contractor", "price", "legal_basic", "end_date", "unit",
                        "last_report_date", "guarantee", "guarantee_period", "warranty_period", "security_percent",
                        "security_sum")


@admin.register(ContractAuction)
class ContractAuctionAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["date", "no_contract", "contractor", "price", "work_scope", "unit", "author"]
    search_fields = ["contractor__name", "no_contract", "unit__county__name", "unit__type__type_short", "unit__city",
                     "worker__name", "worker__last_name", 'investments_project__project_title']
    filter_horizontal = ["worker"]
    autocomplete_fields = ['worker', 'contractor', 'unit']
    list_display_links = ("no_contract",)
    resources_class = ContractAuctionResource


@admin.register(AnnexContractAuction)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["date", "price_change", "price_after_change", "author"]


class LegalBasicResource(resources.ModelResource):
    act = Field(attribute="act", column_name="Ustawa")
    legal_basic = Field(attribute="legal_basic", column_name="Paragraf")
    legal_basic_text = Field(attribute="legal_basic_text", column_name="Tekst paragrafu")

    class Meta:
        model = LegalBasic
        fields = ("act", "legal_basic", "legal_basic_text")
        export_order = ("act", "legal_basic", "legal_basic_text")


@admin.register(LegalBasic)
class LegalBasicAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["act", "legal_basic", "legal_basic_text"]
    resource_class = LegalBasicResource


@admin.register(MediaType)
class ContractMediaAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "folders_type"]
    list_display_links = ("type",)


class ContractMediaResource(resources.ModelResource):
    date = Field(attribute="date", column_name="Data umowy")
    no_contract = Field(attribute="no_contract", column_name="Nr. umowy")
    contractor = Field(attribute="contractor", column_name="Kontrahent")
    type = Field(attribute="type", column_name="Rodzaj umoww")
    legal_basic = Field(attribute="legal_basic", column_name="Tryb UPZP")
    content = Field(attribute="content", column_name="Treśc")
    period_of_validity = Field(attribute="period_of_validity", column_name="Termin umowy")
    unit = Field(attribute="unit", column_name="Jednostka", widget=ManyToManyWidget(Unit, f", \n", field="full_name"))
    information = Field(attribute="information", column_name="Informacje")
    employer = Field(attribute="employer", column_name="Branżysta")
    state = Field(attribute="Stan", column_name="Aktualna")

    class Meta:
        model = ContractMedia
        fields = ("__all__")
        export_order = (
            "date", "no_contract", "contractor", "type", "legal_basic", "content", "period_of_validity", "unit",
            "state", "employer")


@admin.register(ContractMedia)
class ContractMediaAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["date", "no_contract", "contractor", "period_of_validity", "type", "state", "author"]
    list_display_links = ("no_contract",)
    filter_horizontal = ["unit"]
    autocomplete_fields = ['contractor']
    resource_class = ContractMediaResource


@admin.register(AnnexContractMedia)
class AnnexContractMediaAdmin(admin.ModelAdmin):
    list_display = ["contract_media", "date", "scope_changes", "author"]
    search_fields = ['contract_media__no_contract']


@admin.register(FinancialDocument)
class FinancialDocumentAdmin(admin.ModelAdmin):
    list_display = ["contract", "date", "no_document", "unit_measure", "value", "vat", "cost_brutto", "author"]
    list_display_links = ["no_document"]
    search_fields = ["contract__no_contract", "no_document"]
