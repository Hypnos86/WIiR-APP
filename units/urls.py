from django.urls import path, re_path
from units.views import units_list, add_unit, archive_units_list, create_units_list_editable,edit_unit, show_all_info_unit

app_name = "units"
urlpatterns = [
    path("units/", create_units_list_editable, name="create_units_list_editable"),
    path("addUnit/", add_unit, name="add_unit"),
    re_path("editUnit/(?P<id>\d+)/$", edit_unit, name="edit_unit"),
    path("unitsArchive/", archive_units_list, name="archive_units_list"),
    re_path("unitInfo/(?P<id>\d+)/$", show_all_info_unit, name="show_all_info_unit"),
    path("", units_list, name="units_list")
]
