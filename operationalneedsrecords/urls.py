from django.urls import path, re_path
from .views import list_needs_letter, new_needs_latter, edit_needs_letter, list_needs_letter_archive, needs_letter_show, \
    show_archive_year_list, show_statistic

app_name = "operationalneedsrecords"
urlpatterns = [
    re_path("needsList/(?P<year>[0-9]{4})/$", list_needs_letter, name="list_needs_letter"),
    path('archiveYearList/', show_archive_year_list, name='show_archive_year_list'),
    re_path("archiveList/(?P<year>[0-9]{4})/$", list_needs_letter_archive, name="list_needs_letter_archive"),
    re_path("addCase/(?P<year>[0-9]{4})/$", new_needs_latter, name="new_needs_latter"),
    re_path("editCase/(?P<year>[0-9]{4})/(?P<id>\d+)/(?P<isFromShow>[\w-]+)?/$", edit_needs_letter, name="edit_needs_letter"),
    re_path("caseInfo/(?P<year>[0-9]{4})/(?P<id>\d+)/$", needs_letter_show, name="needs_letter_show"),
    re_path("statistics/(?P<year>[0-9]{4})/$", show_statistic, name="show_statistic")
]
