from django.urls import path
from units.views import units_list, add_unit, archive_units_list, create_units_list_editable,edit_unit, show_all_info_unit

app_name = "units"
urlpatterns = [
    path("jednostki/", create_units_list_editable, name="create_units_list_editable"),
    path("dodaj_jednostek/", add_unit, name="add_unit"),
    path("edytuj_jednostek/<int:id>/", edit_unit, name="edit_unit"),
    path("archiwum_jednostek/", archive_units_list, name="archive_units_list"),
    path("informacje/<int:id>/", show_all_info_unit, name="show_all_info_unit"),
    path("", units_list, name="units_list")
]
