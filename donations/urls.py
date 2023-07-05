from django.urls import path, re_path
from donations.views import DonationsListView, AddDonationView, edit_donation, ShowInformationView, DonationsArchiveYearListView, \
    DonationsArchiveListView

app_name = 'donations'

urlpatterns = [
    path('<int:year>/', DonationsListView.as_view(), name='donations_list'),
    re_path('new/(?P<year>[0-9]{4})/$', AddDonationView.as_view(), name='add_donation'),
    re_path('edit/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', edit_donation, name='edit_donation'),
    re_path('info/(?P<id>\d+)/$', ShowInformationView.as_view(), name='show_information_popup'),
    path('year/', DonationsArchiveYearListView.as_view(), name='show_archive_year_list'),
    re_path('archive/year/(?P<year>[0-9]{4})/$', DonationsArchiveListView.as_view(), name='donations_list_archive')
]
