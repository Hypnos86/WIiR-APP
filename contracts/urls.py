from django.urls import path
from contracts.views import menu_contracts, new_contracts

app_name = 'contracts'
urlpatterns = [
    path('', menu_contracts, name='menu_contracts'),
    path('newcontract/', new_contracts, name='new_contracts')
]
