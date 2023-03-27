from django.urls import path, re_path
from contracts.views import menu_contractsimmovables, menu_contractsimmovables_archive, new_contractsimmovables, \
    edit_contractsimmovables, show_contractsimmovables, menu_contracts_auction, new_contract_auction, \
    show_contract_auction, edit_contract_auction, add_annex_immovables, add_annex_contract_auction, \
    contract_media_list, contract_media_list_archive, new_contract_media, edit_contract_media, show_contract_media, \
    add_annex_contract_media, edit_settlement, show_information_settlement, financial_document_list, \
    add_financial_document,edit_financial_document

app_name = "contracts"
urlpatterns = [
    path("contractImmovable/", menu_contractsimmovables, name="menu_contractsimmovables"),
    path("contractImmovable/archive/", menu_contractsimmovables_archive, name="menu_contractsimmovables_archive"),
    path("contractImmovable/new/", new_contractsimmovables, name="new_contractsimmovables"),
    re_path("contractImmovable/edit/(?P<id>\d+)/$", edit_contractsimmovables, name="edit_contractsimmovables"),
    re_path("contractImmovable/info/(?P<id>\d+)/$", show_contractsimmovables, name="show_contractsimmovables"),
    re_path("contractImmovable/new/annex/(?P<id>\d+)/$", add_annex_immovables, name="add_annex_immovables"),
    path("contractZzp/", menu_contracts_auction, name="menu_contracts_auction"),
    path("contractZzp/new/", new_contract_auction, name="new_contract_auction"),
    re_path("contractZzp/edit/(?P<id>\d+)/$", edit_contract_auction, name="edit_contract_auction"),
    re_path("contractZzp/info/(?P<id>\d+)/$", show_contract_auction, name="show_contract_auction"),
    re_path("contractZzp/new/annex/(?P<id>\d+)/$", add_annex_contract_auction, name="add_annex_contract_auction"),
    path("contractMedia/", contract_media_list, name="create_contract_media_list"),
    path("contractMedia/archive/", contract_media_list_archive, name="contract_media_list_archive"),
    re_path("contractMedia/financialDoc/(?P<contract_id>\d+)/$", financial_document_list, name="financial_document_list"),
    re_path("contractMedia/financialDoc/new/(?P<contract_id>\d+)/$", add_financial_document, name="add_financial_document"),
    re_path("contractMedia/financialDoc/edit/(?P<contract_id>\d+)/(?P<info_id>\d+)/$", edit_financial_document, name="edit_financial_document"),
    path("contractMedia/new/", new_contract_media, name="new_contract_media"),
    re_path("contractMedia/edit/(?P<id>\d+)/$", edit_contract_media, name="edit_contract_media"),
    re_path("contractMedia/info/(?P<id>\d+)/$", show_contract_media, name="show_contract_media"),
    re_path("addAnnexMedia/(?P<id>\d+)/$", add_annex_contract_media, name="add_annex_contract_media"),
    re_path("settlementForm/(?P<id>\d+)/$", edit_settlement, name="edit_settlement"),
    re_path("settlementPopup/(?P<id>\d+)/$", show_information_settlement, name="show_information_settlement")
]
