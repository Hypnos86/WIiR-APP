from django.urls import path
from .views import list_needs_letter, new_needs_latter, edit_needs_letter

app_name = "operationalneedsrecords"
urlpatterns = [
    path("ewidencja_zdarzen/", list_needs_letter, name="list_needs_letter"),
    path("add_letter/", new_needs_latter, name="new_needs_latter"),
    path("edit_letter/<int:id>", edit_needs_letter, name="edit_needs_letter")
]
