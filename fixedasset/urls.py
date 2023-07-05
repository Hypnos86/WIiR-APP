from django.urls import path, re_path
from fixedasset.views import FixedAssetListView, ShowInformationView, AddBuildingView, edit_building

app_name = "fixedasset"

urlpatterns = [
    path("buildings/", FixedAssetListView.as_view(), name="fixed_asset_list"),
    re_path("buildings/info/(?P<id>\d+)/$", ShowInformationView.as_view(), name="show_information"),
    path("buildings/add/", AddBuildingView.as_view(), name="add_new_building"),
    re_path("buildings/edit/(?P<id>\d+)/$", edit_building, name="edit_building")
]
