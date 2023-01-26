from django.urls import path
from .views import list_needs_letter, new_needs_latter

app_name = "operationalneedsrecords"
urlpatterns = [
    path("ewidencja_zdarzen/", list_needs_letter, name="list_needs_letter"),
    path("add_new_letter", new_needs_latter, name="new_needs_latter")
]
