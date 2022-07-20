from django.urls import path
from units.views import units_list, add_unit, archive_units_list, create_units_list_editable,edit_unit

app_name = 'units'
urlpatterns = [
    path('units', create_units_list_editable, name='create_units_list_editable'),
    path('add_unit', add_unit, name="add_unit"),
    path('edit_unit', edit_unit, name='edit_unit'),
    path('archiwum', archive_units_list, name="archive_units_list"),
    path('', units_list, name="units_list")
]
