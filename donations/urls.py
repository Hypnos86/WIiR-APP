from django.urls import path
from donations.views import donations_list, add_donation, edit_donation, show_information_popup, show_archive_year_list

app_name = 'donations'

urlpatterns = [
    path('donations/', donations_list, name='donations_list'),
    path('add_donation/', add_donation, name='add_donation'),
    path('edit_donation/<int:id>', edit_donation, name='edit_donation'),
    path('information/<int:id>', show_information_popup, name='show_information_popup'),
    path('archive_year_donation_list/', show_archive_year_list, name='show_archive_year_list')
]
