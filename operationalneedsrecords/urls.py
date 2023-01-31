from django.urls import path
from .views import list_needs_letter, new_needs_latter, edit_needs_letter, list_needs_letter_archive, needs_letter_show, \
    show_archive_year_list

app_name = "operationalneedsrecords"
urlpatterns = [
    path("needs_list/<int:year>/", list_needs_letter, name="list_needs_letter"),
    path('archive_year_list/', show_archive_year_list, name='show_archive_year_list'),
    path("archive_list/<int:year>/", list_needs_letter_archive, name="list_needs_letter_archive"),
    path("add_case/<int:year>/", new_needs_latter, name="new_needs_latter"),
    path("edit_case/<int:year>/<int:id>", edit_needs_letter, name="edit_needs_letter"),
    path("case/<int:year>/<int:id>/", needs_letter_show, name="needs_letter_show")
]
