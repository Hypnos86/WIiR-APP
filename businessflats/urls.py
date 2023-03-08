from django.urls import path, re_path
from businessflats.views import FlatsListView, AddNewFlatView, EditFlatView, ShowInformationView

app_name = "businessflats"
urlpatterns = [

    path("add_flat/", AddNewFlatView.as_view(), name="add_new_flat"),
    re_path("edit_flat/(?P<id>\d+)/$", EditFlatView.as_view(), name="edit_flat"),
    re_path("info/(?P<id>\d+)/$", ShowInformationView.as_view(), name="show_information"),
    path("", FlatsListView.as_view(), name="make_flats_list")
]
