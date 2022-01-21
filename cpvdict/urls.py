from django.urls import path
from cpvdict.views import cpvlist, type_expense_list, order_list, new_order, type_work_list, edit_order

app_name = 'cpvdict'
urlpatterns = [
    path('cpv_dictionary/', cpvlist, name='cpvlist'),
    path('rodzajowosc/', type_expense_list, name='type_expense_list'),
    path('rodzajowosc_rb/', type_work_list, name='type_work_list'),
    path('order_list/', order_list, name='order_list'),
    path('new_order/', new_order, name='new_order'),
    path('edit_order/<int:id>', edit_order, name='edit_order')
]
