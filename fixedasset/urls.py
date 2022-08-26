from django.urls import path
from fixedasset.views import fixed_asset_list, show_information

app_name = "fixedasset"

urlpatterns = [
    path("fixed_asset/", fixed_asset_list, name="fixed_asset_list"),
    path("info_popup/<int:id>", show_information, name="show_information")
]
