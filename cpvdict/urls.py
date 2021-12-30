from django.urls import path
from cpvdict.views import cpvlist, type_expense_list, order_list, new_order

app_name = 'cpvdict'
urlpatterns = [
    path('slownikcpv/', cpvlist, name='cpvlist'),
    path('rodzajowosc/', type_expense_list, name='type_expense_list'),
    path('lista_zlecen/', order_list, name='order_list'),
    path('nowe_zlecenie/', new_order, name='new_order')
]
