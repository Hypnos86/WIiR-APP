from django.urls import path
from cpvdict.views import cpvlist, type_expense_list, order_list, show_order_info_popup, new_order, type_work_list, \
    show_information_work_object, edit_order, make_archive_year_list, create_order_archive

app_name = 'cpvdict'
urlpatterns = [
    path('slownik_cpv/', cpvlist, name='cpvlist'),
    path('rodzajowosc/', type_expense_list, name='type_expense_list'),
    path('rodzajowosc_rb/', type_work_list, name='type_work_list'),
    path('informacje/<int:id>', show_information_work_object, name='show_information_work_object'),
    path('lista_zlecen/', order_list, name='order_list'),
    path('show_information<int:id>', show_order_info_popup, name='show_order_info_popup'),
    path('nowe_zlecenie/', new_order, name='new_order'),
    path('edycja_zlecenia/<int:id>', edit_order, name='edit_order'),
    path('arichive_list_year', make_archive_year_list, name='make_archive_year_list'),
    path('archive_list_order/<int:year>', create_order_archive, name='create_order_archive')
]
