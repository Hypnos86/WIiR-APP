from django.urls import path
from .views import contractor_list, new_contractor, edit_contractor, show_information

app_name = "contractors"
urlpatterns = [
    path("newContractor/", new_contractor, name="new_contractor"),
    path("editContractor/<int:id>/", edit_contractor, name="edit_contractor"),
    path("info/<int:id>/", show_information, name="show_information"),
    path("", contractor_list, name="contractor_list")
]
