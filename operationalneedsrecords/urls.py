from django.urls import path, re_path
from .views import NeedsLetterListView, NewNeedsLetterView, EditNeedsLetterView, NeedsLetterArchiveView, ShowNeedsLetterView, \
    ArchiveYearListView, StatisticView

app_name = "operationalneedsrecords"
urlpatterns = [
    re_path("(?P<year>[0-9]{4})/$", NeedsLetterListView.as_view(), name="list_needs_letter"),
    path('yearListArchive/', ArchiveYearListView.as_view(), name='show_archive_year_list'),
    re_path("archive/(?P<year>[0-9]{4})/$", NeedsLetterArchiveView.as_view(), name="list_needs_letter_archive"),
    re_path("add/(?P<year>[0-9]{4})/$", NewNeedsLetterView.as_view(), name="new_needs_latter"),
    re_path("edit/(?P<year>[0-9]{4})/(?P<id>\d+)/(?P<isFromShow>[\w-]+)?/$", EditNeedsLetterView.as_view(), name="edit_needs_letter"),
    re_path("(?P<year>[0-9]{4})/info/(?P<id>\d+)/$", ShowNeedsLetterView.as_view(), name="needs_letter_show"),
    re_path("(?P<year>[0-9]{4})/statistics/$", StatisticView.as_view(), name="show_statistic")
]
