from django.urls import path
from contracts.views import menu_contractsimmovables, new_contractsimmovables, edit_contractsimmovables, \
    show_contractsimmovables, new_aneks, menu_contracts_auction, new_contract_auction

app_name = 'contracts'
urlpatterns = [
    path('', menu_contractsimmovables, name='menu_contractsimmovables'),
    path('newcontractimmovables/', new_contractsimmovables, name='new_contractsimmovables'),
    path('editcontractimmovables/<int:id>', edit_contractsimmovables, name='edit_contractsimmovables'),
    path('showcontractimmovables/<int:id>', show_contractsimmovables, name='show_contractsimmovables'),
    path('newaneks/', new_aneks, name='new_aneks'),
    path('contract_auction/', menu_contracts_auction, name='menu_contracts_auction'),
    path('new_contract_zzp/', new_contract_auction, name='new_contract_auction')
]
