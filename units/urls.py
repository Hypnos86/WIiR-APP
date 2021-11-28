from django.urls import path
from .views import make_units_list

app_name = 'units'
urlpatterns = [
    path('', make_units_list, name="unitlist")
]
