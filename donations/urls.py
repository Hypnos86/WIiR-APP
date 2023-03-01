from django.urls import path,re_path
from donations.views import donations_list, add_donation, edit_donation, show_information_popup, show_archive_year_list, donations_list_archive

app_name = 'donations'

urlpatterns = [
    path('donations/<int:year>/', donations_list, name='donations_list'),
    re_path('newDonation/(?P<id>\d+)/$', add_donation, name='add_donation'),
    re_path('editDonation/(?P<year>[0-9]{4})/(?P<id>\d+)/$', edit_donation, name='edit_donation'),
    re_path('info/(?P<id>\d+)/$', show_information_popup, name='show_information_popup'),
    path('donationYear/', show_archive_year_list, name='show_archive_year_list'),
    re_path('donationArchive/(?P<year>[0-9]{4})/$', donations_list_archive, name='donations_list_archive')
]
