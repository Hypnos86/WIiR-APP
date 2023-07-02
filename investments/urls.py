from django.urls import path, re_path
from investments.views import ImportantTaskInvestments, InvestmentProjectsList, AddProjectView, EditProjectView, \
    ShowProjectView, ShowGalleriesView, AddContractToProject

app_name = "investments"
urlpatterns = [
    path("menu/list/", InvestmentProjectsList.as_view(), name="investment_projects_list"),
    path("menu/list/new/", AddProjectView.as_view(), name="add_new_project"),
    re_path("menu/list/edit/(?P<id>\d+)/$", EditProjectView.as_view(), name="edit_project"),
    re_path("menu/list/show/(?P<id>\d+)/$", ShowProjectView.as_view(), name="show_project"),
    re_path("gallery/(?P<id>\d+)/$", ShowGalleriesView.as_view(), name="show_galleries_popup"),
    re_path("menu/list/addToProject/(?P<id>\d+)/$", AddContractToProject.as_view(), name="add_contract_to_project"),
    path("menu/", ImportantTaskInvestments.as_view(), name="make_important_task_investments")

]
