from django.urls import path
from units.views import units_list, add_unit

app_name = 'units'
urlpatterns = [
    path('addunit', add_unit, name="add_unit"),
    path('', units_list, name="units_list")
]
