from django.urls import path
from contracts.views import menu_contractsimmovables, menu_contractsimmovables_archive,new_contractsimmovables, edit_contractsimmovables, \
    show_contractsimmovables, menu_contracts_auction, new_contract_auction, show_contract_auction, \
    edit_contract_auction, add_annex_immovables

app_name = 'contracts'
urlpatterns = [
    path('lista_umow/', menu_contractsimmovables, name='menu_contractsimmovables'),
    path('lista_umow_archiwum/', menu_contractsimmovables_archive, name='menu_contractsimmovables_archive'),
    path('nowa_umowa_nieruchomosci/', new_contractsimmovables, name='new_contractsimmovables'),
    path('edycja_umowy_nieruchomosci/<int:id>', edit_contractsimmovables, name='edit_contractsimmovables'),
    path('podglad_umowy_nieruchomosci/<int:id>', show_contractsimmovables, name='show_contractsimmovables'),
    path('dodaj_aneks_umowy_nieruchomosci/<int:id>', add_annex_immovables, name='add_annex_immovables'),
    path('umowy_przetargowe/', menu_contracts_auction, name='menu_contracts_auction'),
    path('nowa_umowa_przetargowa/', new_contract_auction, name='new_contract_auction'),
    path('edycja_umowy_przetargowej/<int:id>', edit_contract_auction, name='edit_contract_auction'),
    path('pogad_umowy_przetargowej/<int:id>', show_contract_auction, name='show_contract_auction')
]
