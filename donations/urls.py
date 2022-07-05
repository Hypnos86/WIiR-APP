from django.urls import path
from donations.views import donations_list, add_donation, edit_donation

app_name = 'donations'

urlpatterns = [
    path('darowizny/', donations_list, name='donations_list'),
    path('dodaj_darowizne/', add_donation, name='add_donation'),
    path('edycja_darowizn/<int:id>', edit_donation, name='edit_donation')
]
