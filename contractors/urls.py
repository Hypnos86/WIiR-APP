from django.urls import path, re_path
from .views import contractor_list, new_contractor, edit_contractor, show_information

app_name = "contractors"
urlpatterns = [
    path("newContractor/", new_contractor, name="new_contractor"),
    re_path("editContractor/(?P<id>\d+)/$", edit_contractor, name="edit_contractor"),
    re_path("info/(?P<id>\d+)/$", show_information, name="show_information"),
    path("", contractor_list, name="contractor_list")
]
