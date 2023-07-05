from django.urls import path, re_path
from .views import UnitListView, AddUnitView, ArchiveUnitsList, create_units_list_editable, edit_unit, ShowAllInfoUnit

app_name = "units"
urlpatterns = [
    path("list/", create_units_list_editable, name="create_units_list_editable"),
    path("list/new/", AddUnitView.as_view(), name="add_unit"),
    re_path("list/edit/(?P<slug>[\w-]+)/$", edit_unit, name="edit_unit"),
    path("list/archive/", ArchiveUnitsList.as_view(), name="archive_units_list"),
    re_path("info/(?P<slug>[\w-]+)/$", ShowAllInfoUnit.as_view(), name="show_all_info_unit"),
    path("", UnitListView.as_view(), name="units_list")
]
