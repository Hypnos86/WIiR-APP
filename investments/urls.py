from django.urls import path
from investments.views import make_important_task_investments, investment_projects_list

app_name = 'investments'
urlpatterns = [
    path('inwestycje/', make_important_task_investments, name='make_important_task_investments'),
    path('zadania_inwestycyjne/', investment_projects_list, name='investment_projects_list')
]
