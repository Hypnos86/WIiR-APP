from django.urls import path
from .views import contractorsell_list, new_contractorsell, edit_contractorsell

app_name = 'contractors'
urlpatterns = [
    path('newcontractorsell/', new_contractorsell, name="new_contractorsell"),
    path('contractorsell/', contractorsell_list, name="contractorssell_list"),
    path('editcontractorsell/<int:id>', edit_contractorsell, name="edit_contractorsell")
]
