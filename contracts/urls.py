from django.urls import path, re_path
from contracts.views import ContractsImmovableListView, ContractsArchiveImmovableListView, NewContractsImmovableView, \
    EditContractImmovablesView, ShowContractImmovableView, ContractsAuctionListView, NewContractAuctionView, \
    ShowContractAuctionView, EditContractAuctionView, AddAnnexImmovablesView, AddAnnexContractAuctionView, \
    ContractMediaListView, ContractsArchiveMediaListView, NewContractMediaView, EditContractMediaView, ShowContractMediaView, \
    AddAnnexContractMediaView, EditSettlementView, ShowSettlementView, FinancialDocumentListView, \
    AddFinancialDocumentView,EditFinancialDocumentView

app_name = "contracts"
urlpatterns = [
    path("contractImmovable/", ContractsImmovableListView.as_view(), name="menu_contractsimmovables"),
    path("contractImmovable/archive/", ContractsArchiveImmovableListView.as_view(), name="menu_contractsimmovables_archive"),
    path("contractImmovable/new/", NewContractsImmovableView.as_view(), name="new_contractsimmovables"),
    re_path("contractImmovable/edit/(?P<id>\d+)/$", EditContractImmovablesView.as_view(), name="edit_contractsimmovables"),
    re_path("contractImmovable/info/(?P<id>\d+)/$", ShowContractImmovableView.as_view(), name="show_contractsimmovables"),
    re_path("contractImmovable/new/annex/(?P<id>\d+)/$", AddAnnexImmovablesView.as_view(), name="add_annex_immovables"),
    path("contractZzp/", ContractsAuctionListView.as_view(), name="menu_contracts_auction"),
    path("contractZzp/new/", NewContractAuctionView.as_view(), name="new_contract_auction"),
    re_path("contractZzp/edit/(?P<id>\d+)/$", EditContractAuctionView.as_view(), name="edit_contract_auction"),
    re_path("contractZzp/info/(?P<id>\d+)/$", ShowContractAuctionView.as_view(), name="show_contract_auction"),
    re_path("contractZzp/new/annex/(?P<id>\d+)/$", AddAnnexContractAuctionView.as_view(), name="add_annex_contract_auction"),
    path("contractMedia/", ContractMediaListView.as_view(), name="create_contract_media_list"),
    path("contractMedia/archive/", ContractsArchiveMediaListView.as_view(), name="contract_media_list_archive"),
    re_path("contractMedia/financialDoc/(?P<contract_id>\d+)/$", FinancialDocumentListView.as_view(), name="financial_document_list"),
    re_path("contractMedia/financialDoc/new/(?P<contract_id>\d+)/$", AddFinancialDocumentView.as_view(), name="add_financial_document"),
    # w wyrazeniach regularnych musza byc te same nazwy parapemtrow zawsze
    re_path("contractMedia/financialDoc/edit/(?P<contract_id>\d+)/(?P<id>\d+)/$", EditFinancialDocumentView.as_view(), name="edit_financial_document"),
    path("contractMedia/new/", NewContractMediaView.as_view(), name="new_contract_media"),
    re_path("contractMedia/edit/(?P<id>\d+)/$", EditContractMediaView.as_view(), name="edit_contract_media"),
    re_path("contractMedia/info/(?P<id>\d+)/$", ShowContractMediaView.as_view(), name="show_contract_media"),
    re_path("addAnnexMedia/(?P<id>\d+)/$", AddAnnexContractMediaView.as_view(), name="add_annex_contract_media"),
    re_path("settlementForm/(?P<id>\d+)/$", EditSettlementView.as_view(), name="edit_settlement"),
    re_path("settlementPopup/(?P<id>\d+)/$", ShowSettlementView.as_view(), name="show_information_settlement")
]
