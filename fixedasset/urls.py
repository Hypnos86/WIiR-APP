from django.urls import path, re_path
from fixedasset.views import fixed_asset_list, show_information, add_new_building, edit_building

app_name = "fixedasset"

urlpatterns = [
    path("recordsBuildings/", fixed_asset_list, name="fixed_asset_list"),
    re_path("infoPopup/(?P<id>\d+)/$", show_information, name="show_information"),
    path("add_Building/", add_new_building, name="add_new_building"),
    re_path("editBuilding/(?P<id>\d+)/$", edit_building, name="edit_building")
]
