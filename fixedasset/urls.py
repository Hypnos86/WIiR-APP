from django.urls import path, re_path
from fixedasset.views import fixed_asset_list, show_information, add_new_building, edit_building

app_name = "fixedasset"

urlpatterns = [
    path("buildings/", fixed_asset_list, name="fixed_asset_list"),
    re_path("buildings/info/(?P<id>\d+)/$", show_information, name="show_information"),
    path("buildings/add/", add_new_building, name="add_new_building"),
    re_path("buildings/edit/(?P<id>\d+)/$", edit_building, name="edit_building")
]
