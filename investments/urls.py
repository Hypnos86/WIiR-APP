from django.urls import path
from investments.views import make_important_task_investments, investment_projects_list, add_new_project, edit_project, \
    show_project, add_contract_to_project

app_name = 'investments'
urlpatterns = [
    path('inwestycje/', make_important_task_investments, name='make_important_task_investments'),
    path('zadania_inwestycyjne/', investment_projects_list, name='investment_projects_list'),
    path('nowe_zadanie_inw/', add_new_project, name='add_new_project'),
    path('edycja_zadania_inw/<int:id>', edit_project, name='edit_project'),
    path('podglad_zadania_inw/<int:id>', show_project, name='show_project'),
    path('podepnii_umowe/<int:id>', add_contract_to_project, name='add_contract_to_project')
]
