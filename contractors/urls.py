from django.urls import path, re_path
from .views import ContractorsListView, AddNewContractorView, EditContractorView, ShowInformationView

app_name = "contractors"
urlpatterns = [
    path("new/", AddNewContractorView.as_view(), name="new_contractor"),
    path("edit/<slug:slug>/", EditContractorView.as_view(), name="edit_contractor"),
    re_path("info/(?P<id>\d+)/$", ShowInformationView.as_view(), name="show_information"),
    path("", ContractorsListView.as_view(), name="contractor_list")
]
