from django.urls import path
from donations.views import donations_list, add_donation, edit_donation, show_information_popup, show_archive_year_list, donations_list_archive

app_name = 'donations'

urlpatterns = [
    path('donations/<int:year>/', donations_list, name='donations_list'),
    path('newDonation/<int:year>/', add_donation, name='add_donation'),
    path('editDonation/<int:year>/<int:id>/', edit_donation, name='edit_donation'),
    path('info<int:id>/', show_information_popup, name='show_information_popup'),
    path('donationYear/', show_archive_year_list, name='show_archive_year_list'),
    path('donationArchive/<int:year>/', donations_list_archive, name='donations_list_archive')
]
