from django.urls import path
from .views import make_units_list, make_new_unit

app_name = 'units'
urlpatterns = [
    path('', make_units_list, name="unitlist")
]
