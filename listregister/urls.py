from django.urls import path
from .views import make_list_register, make_flats_list, add_new_flat, edit_flat, show_information

app_name = 'listregister'
urlpatterns = [
    path('ewidencja/', make_list_register, name='make_list_register'),
    path('lista_mieszkan/', make_flats_list, name='make_flats_list'),
    path('dodaj_nowy_lokal/', add_new_flat, name='add_new_flat'),
    path('edytowanie_lokalu/<int:id>', edit_flat, name='edit_flat'),
    path('informacje/<int:id>', show_information, name='show_information')
]
