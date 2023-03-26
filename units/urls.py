from django.urls import path, re_path
from .views import UnitList, add_unit, ArchiveUnitsList, create_units_list_editable, edit_unit, ShowAllInfoUnit

app_name = "units"
urlpatterns = [
    path("units/", create_units_list_editable, name="create_units_list_editable"),
    path("new/", add_unit, name="add_unit"),
    re_path("edit/(?P<id>\d+)/$", edit_unit, name="edit_unit"),
    path("archive/", ArchiveUnitsList.as_view(), name="archive_units_list"),
    re_path("info/(?P<id>\d+)/$", ShowAllInfoUnit.as_view(), name="show_all_info_unit"),
    path("", UnitList.as_view(), name="units_list")
]
