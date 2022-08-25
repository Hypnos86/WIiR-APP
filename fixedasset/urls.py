from django.urls import path
from fixedasset.views import fixed_asset_list

app_name = "fixedasset"

urlpatterns = [
    path("fixed_asset/", fixed_asset_list, name="fixed_asset_list")
]
