from django.urls import path
from investments.views import make_important_task_investments, investment_projects_list, add_new_project, edit_project, \
    show_project, show_galleries_popup ,add_contract_to_project

app_name = 'investments'
urlpatterns = [
    path('inwestycje/', make_important_task_investments, name='make_important_task_investments'),
    path('zadania_inwestycyjne/', investment_projects_list, name='investment_projects_list'),
    path('new_investments/', add_new_project, name='add_new_project'),
    path('edit_investment/<int:id>', edit_project, name='edit_project'),
    path('show_investment/<int:id>', show_project, name='show_project'),
    path("project_gallery/<int:id>", show_galleries_popup, name='show_galleries_popup'),
    path('add_contract_to_project/<int:id>', add_contract_to_project, name='add_contract_to_project')
]
