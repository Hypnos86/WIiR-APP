from django.urls import path
from donations.views import donations_list, add_donation, edit_donation, show_information_popup, show_archive_year_list, donations_list_archive

app_name = 'donations'

urlpatterns = [
    path('darowizny/<int:year>/', donations_list, name='donations_list'),
    path('nowa_darowizna/<int:year>/', add_donation, name='add_donation'),
    path('edycja_darowizny/<int:year>/<int:id>/', edit_donation, name='edit_donation'),
    path('informacje/<int:id>/', show_information_popup, name='show_information_popup'),
    path('lata_darowizn/', show_archive_year_list, name='show_archive_year_list'),
    path('archiwum_darowizn/<int:year>/', donations_list_archive, name='donations_list_archive')
]
