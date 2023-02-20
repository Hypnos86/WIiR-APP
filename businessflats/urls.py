from django.urls import path, re_path
from businessflats.views import make_flats_list, add_new_flat, edit_flat, show_information

app_name = "businessflats"
urlpatterns = [

    path("add_flat/", add_new_flat, name="add_new_flat"),
    re_path("edit_flat/(?P<id>\d+)/$", edit_flat, name="edit_flat"),
    re_path("info/(?P<id>\d+)/$", show_information, name="show_information"),
    path("", make_flats_list, name="make_flats_list")
]
