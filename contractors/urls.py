from django.urls import path
from .views import contractor_list, new_contractor, edit_contractor, show_information

app_name = 'contractors'
urlpatterns = [
    path('nowy_kontrahent/', new_contractor, name="new_contractor"),
    path('kontrahenci/', contractor_list, name="contractor_list"),
    path('edycja_kontrahenta/<int:id>', edit_contractor, name="edit_contractor"),
    path('informacje/<int:id>', show_information, name='show_information')
]
