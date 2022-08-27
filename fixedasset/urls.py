from django.urls import path
from fixedasset.views import fixed_asset_list, show_information, add_new_building, edit_building

app_name = "fixedasset"

urlpatterns = [
    path("", fixed_asset_list, name="fixed_asset_list"),
    path("info_popup/<int:id>", show_information, name="show_information"),
    path("add_building/", add_new_building, name="add_new_building"),
    path("edit_building/<int:id>", edit_building, name="edit_building")
]
