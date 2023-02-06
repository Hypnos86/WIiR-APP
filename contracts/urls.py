from django.urls import path
from contracts.views import menu_contractsimmovables, menu_contractsimmovables_archive, new_contractsimmovables, \
    edit_contractsimmovables, show_contractsimmovables, menu_contracts_auction, new_contract_auction, \
    show_contract_auction, edit_contract_auction, add_annex_immovables, add_annex_contract_auction, \
    contract_media_list, contract_media_list_archive, new_contract_media, edit_contract_media, show_contract_media, \
    add_annex_contract_media, edit_settlement, show_information_settlement, financial_document_list, \
    add_financial_document,edit_financial_document

app_name = "contracts"
urlpatterns = [
    path("", menu_contractsimmovables, name="menu_contractsimmovables"),
    path("archiveContractImmovable/", menu_contractsimmovables_archive, name="menu_contractsimmovables_archive"),
    path("newContractImmovable/", new_contractsimmovables, name="new_contractsimmovables"),
    path("editContractImmovable/<int:id>/", edit_contractsimmovables, name="edit_contractsimmovables"),
    path("contractImmovable/<int:id>/", show_contractsimmovables, name="show_contractsimmovables"),
    path("addAnnexImmovable/<int:id>/", add_annex_immovables, name="add_annex_immovables"),
    path("contractZzp/", menu_contracts_auction, name="menu_contracts_auction"),
    path("newContractZzp/", new_contract_auction, name="new_contract_auction"),
    path("editContract_zpp/<int:id>/", edit_contract_auction, name="edit_contract_auction"),
    path("contractZzp/<int:id>/", show_contract_auction, name="show_contract_auction"),
    path("addAnnexZzp/<int:id>/", add_annex_contract_auction, name="add_annex_contract_auction"),
    path("contractMediaList/", contract_media_list, name="create_contract_media_list"),
    path("contractMediaListArchive/", contract_media_list_archive, name="contract_media_list_archive"),
    path("financialDoc/<int:contract_id>/", financial_document_list, name="financial_document_list"),
    path("newFinancialDoc/<int:contract_id>/", add_financial_document, name="add_financial_document"),
    path("editFinancialDoc/<int:contract_id>/<int:id>/", edit_financial_document, name="edit_financial_document"),
    path("newContractMedia/", new_contract_media, name="new_contract_media"),
    path("editContractMedia/<int:id>/", edit_contract_media, name="edit_contract_media"),
    path("contractMedia/<int:id>/", show_contract_media, name="show_contract_media"),
    path("addAnnexMedia/<int:id>/", add_annex_contract_media, name="add_annex_contract_media"),
    path("settlementForm/<int:id>/", edit_settlement, name="edit_settlement"),
    path("settlementPopup/<int:id>/", show_information_settlement, name="show_information_settlement")
]
