from django.urls import path
from businessflats.views import make_flats_list, add_new_flat, edit_flat, show_information

app_name = "businessflats"
urlpatterns = [
    path("lista_lokali/", make_flats_list, name="make_flats_list"),
    path("dodaj_nowy_lokal/", add_new_flat, name="add_new_flat"),
    path("edytowanie_lokalu/<int:id>", edit_flat, name="edit_flat"),
    path("informacje/<int:id>", show_information, name="show_information")
]
