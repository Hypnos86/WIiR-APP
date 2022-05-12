from django.urls import path
from investments.views import investments_list, investment_projects_list

app_name = 'investments'
urlpatterns = [
    path('inwestycje/', investments_list, name='investments_list'),
    path('zadania_inwestycyjne/', investment_projects_list, name='investment_projects_list')
]
