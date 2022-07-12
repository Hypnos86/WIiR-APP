from django.urls import path
from donations.views import donations_list, add_donation, edit_donation, show_information_popup

app_name = 'donations'

urlpatterns = [
    path('darowizny/', donations_list, name='donations_list'),
    path('dodaj_darowizne/', add_donation, name='add_donation'),
    path('edycja_darowizn/<int:id>', edit_donation, name='edit_donation'),
    path('information/<int:id>', show_information_popup, name='show_information_popup')
]
