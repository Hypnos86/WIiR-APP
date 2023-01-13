from django.urls import path
from contracts.views import menu_contractsimmovables, menu_contractsimmovables_archive, new_contractsimmovables, \
    edit_contractsimmovables, show_contractsimmovables, menu_contracts_auction, new_contract_auction, \
    show_contract_auction, edit_contract_auction, add_annex_immovables, add_annex_contract_auction, \
    contract_media_list, new_contract_media, edit_contract_media, show_contract_media, add_annex_contract_media, edit_settlement, show_information_settlement

app_name = "contracts"
urlpatterns = [
    path("", menu_contractsimmovables, name="menu_contractsimmovables"),
    path("archive_contract_immovable/", menu_contractsimmovables_archive, name="menu_contractsimmovables_archive"),
    path("new_contract_immovable/", new_contractsimmovables, name="new_contractsimmovables"),
    path("edit_contract_immovable/<int:id>", edit_contractsimmovables, name="edit_contractsimmovables"),
    path("contract_immovable/<int:id>", show_contractsimmovables, name="show_contractsimmovables"),
    path("add_annex_immovable/<int:id>", add_annex_immovables, name="add_annex_immovables"),
    path("contract_zzp/", menu_contracts_auction, name="menu_contracts_auction"),
    path("new_contract_zzp/", new_contract_auction, name="new_contract_auction"),
    path("edit_contract_zpp/<int:id>", edit_contract_auction, name="edit_contract_auction"),
    path("contract_zzp/<int:id>", show_contract_auction, name="show_contract_auction"),
    path("add_annex_zzp/<int:id>", add_annex_contract_auction, name="add_annex_contract_auction"),
    path("contract_media_list", contract_media_list, name="create_contract_media_list"),
    path("new_contract_media", new_contract_media, name="new_contract_media"),
    path("edit_contract_media/<int:id>", edit_contract_media, name="edit_contract_media"),
    path("contract_media/<int:id>", show_contract_media, name="show_contract_media"),
    path("add_annex_media/<int:id>", add_annex_contract_media, name="add_annex_contract_media"),
    path("settlement_form/<int:id>", edit_settlement, name="edit_settlement"),
    path("settlement_popup/<int:id>", show_information_settlement, name="show_information_settlement")
]
