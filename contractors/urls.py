from django.urls import path
from .views import contractor_list, new_contractor, edit_contractor, show_information

app_name = "contractors"
urlpatterns = [
    path("new_contractor/", new_contractor, name="new_contractor"),
    path("edit_contractor/<int:id>", edit_contractor, name="edit_contractor"),
    path("information/<int:id>", show_information, name="show_information"),
    path("", contractor_list, name="contractor_list")
]
