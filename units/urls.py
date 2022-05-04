from django.urls import path
from units.views import units_list, add_unit, archive_units_list

app_name = 'units'
urlpatterns = [
    path('addunit', add_unit, name="add_unit"),
    path('archiwum', archive_units_list, name="archive_units_list"),
    path('', units_list, name="units_list")
]
