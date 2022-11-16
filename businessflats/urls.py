from django.urls import path
from businessflats.views import make_flats_list, add_new_flat, edit_flat, show_information

app_name = "businessflats"
urlpatterns = [
    path("add_flat/", add_new_flat, name="add_new_flat"),
    path("edit_flat/<int:id>", edit_flat, name="edit_flat"),
    path("information/<int:id>", show_information, name="show_information"),
    path("", make_flats_list, name="make_flats_list")
]
