from django.urls import path
from .views import contractorsell_list, new_contractorsell, edit_contractorsell, show_information

app_name = 'contractors'
urlpatterns = [
    path('nowy_kontrahent/', new_contractorsell, name="new_contractorsell"),
    path('kontrahenci/', contractorsell_list, name="contractorssell_list"),
    path('edycja_kontrahenta/<int:id>', edit_contractorsell, name="edit_contractorsell"),
    path('informacje/<int:id>', show_information, name='show_information')
]
