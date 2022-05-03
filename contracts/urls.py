from django.urls import path
from contracts.views import menu_contractsimmovables, new_contractsimmovables, edit_contractsimmovables, \
    show_contractsimmovables, menu_contracts_auction, new_contract_auction, show_contract_auction, \
    edit_contract_auction, add_annex_immovables

app_name = 'contracts'
urlpatterns = [
    path('', menu_contractsimmovables, name='menu_contractsimmovables'),
    path('new_contract_immovables/', new_contractsimmovables, name='new_contractsimmovables'),
    path('edit_contract_immovables/<int:id>', edit_contractsimmovables, name='edit_contractsimmovables'),
    path('show_contract_immovables/<int:id>', show_contractsimmovables, name='show_contractsimmovables'),
    path('add_annex_immovables/<int:id>', add_annex_immovables, name='add_annex_immovables'),
    path('contract_auction/', menu_contracts_auction, name='menu_contracts_auction'),
    path('new_contract_zzp/', new_contract_auction, name='new_contract_auction'),
    path('edit_contract_zzp/<int:id>', edit_contract_auction, name='edit_contract_auction'),
    path('show_contract_auction/<int:id>', show_contract_auction, name='show_contract_auction')
]
