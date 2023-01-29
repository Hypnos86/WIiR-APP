from django.urls import path
from .views import list_needs_letter, new_needs_latter, edit_needs_letter, list_needs_letter_archive, needs_letter_show

app_name = "operationalneedsrecords"
urlpatterns = [
    path("lista_pism/<int:year>/", list_needs_letter, name="list_needs_letter"),
    path("archiwum_pism/<int:year>/", list_needs_letter_archive, name="list_needs_letter_archive"),
    path("dodaj_sprawe/<int:year>/", new_needs_latter, name="new_needs_latter"),
    path("edycja_sprawy/<int:year>/<int:id>", edit_needs_letter, name="edit_needs_letter"),
    path("sprawa/<int:year>/<int:id>/", needs_letter_show, name="needs_letter_show")
]
