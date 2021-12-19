from django.urls import path
from cpvdict.views import cpvlist, type_expense_list

app_name = 'cpvdict'
urlpatterns = [
    path('slownikcpv/', cpvlist, name='cpvlist'),
    path('rodzajowosc/', type_expense_list, name='type_expense_list')
]
