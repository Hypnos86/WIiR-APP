from django.urls import path, re_path
from contracts.views import ContractsImmovableListView, ContractsArchiveImmovableListView, NewContractsImmovableView, \
    edit_contractsimmovables, ShowContractImmovableView, ContractsAuctionListView, new_contract_auction, \
    ShowContractAuctionView, edit_contract_auction, add_annex_immovables, add_annex_contract_auction, \
    ContractMediaListView, ContractsArchiveMediaListView, new_contract_media, edit_contract_media, ShowContractMediaView, \
    add_annex_contract_media, EditSettlementView, ShowSettlementView, FinancialDocumentListView, \
    add_financial_document,edit_financial_document

app_name = "contracts"
urlpatterns = [
    path("contractImmovable/", ContractsImmovableListView.as_view(), name="menu_contractsimmovables"),
    path("contractImmovable/archive/", ContractsArchiveImmovableListView.as_view(), name="menu_contractsimmovables_archive"),
    path("contractImmovable/new/", NewContractsImmovableView.as_view(), name="new_contractsimmovables"),
    re_path("contractImmovable/edit/(?P<id>\d+)/$", edit_contractsimmovables, name="edit_contractsimmovables"),
    re_path("contractImmovable/info/(?P<id>\d+)/$", ShowContractImmovableView.as_view(), name="show_contractsimmovables"),
    re_path("contractImmovable/new/annex/(?P<id>\d+)/$", add_annex_immovables, name="add_annex_immovables"),
    path("contractZzp/", ContractsAuctionListView.as_view(), name="menu_contracts_auction"),
    path("contractZzp/new/", new_contract_auction, name="new_contract_auction"),
    re_path("contractZzp/edit/(?P<id>\d+)/$", edit_contract_auction, name="edit_contract_auction"),
    re_path("contractZzp/info/(?P<id>\d+)/$", ShowContractAuctionView.as_view(), name="show_contract_auction"),
    re_path("contractZzp/new/annex/(?P<id>\d+)/$", add_annex_contract_auction, name="add_annex_contract_auction"),
    path("contractMedia/", ContractMediaListView.as_view(), name="create_contract_media_list"),
    path("contractMedia/archive/", ContractsArchiveMediaListView.as_view(), name="contract_media_list_archive"),
    re_path("contractMedia/financialDoc/(?P<contract_id>\d+)/$", FinancialDocumentListView.as_view(), name="financial_document_list"),
    re_path("contractMedia/financialDoc/new/(?P<contract_id>\d+)/$", add_financial_document, name="add_financial_document"),
    re_path("contractMedia/financialDoc/edit/(?P<contract_id>\d+)/(?P<info_id>\d+)/$", edit_financial_document, name="edit_financial_document"),
    path("contractMedia/new/", new_contract_media, name="new_contract_media"),
    re_path("contractMedia/edit/(?P<id>\d+)/$", edit_contract_media, name="edit_contract_media"),
    re_path("contractMedia/info/(?P<id>\d+)/$", ShowContractMediaView.as_view(), name="show_contract_media"),
    re_path("addAnnexMedia/(?P<id>\d+)/$", add_annex_contract_media, name="add_annex_contract_media"),
    re_path("settlementForm/(?P<id>\d+)/$", EditSettlementView.as_view(), name="edit_settlement"),
    re_path("settlementPopup/(?P<id>\d+)/$", ShowSettlementView.as_view(), name="show_information_settlement")
]
