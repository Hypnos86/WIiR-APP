from django.urls import path
from investments.views import investments_list

app_name = 'investments'

urlpatterns = [
    path('inwestycje/', investments_list, name='investments_list')
]
