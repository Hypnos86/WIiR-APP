from django.urls import path, re_path
from investments.views import make_important_task_investments, investment_projects_list, add_new_project, edit_project, \
    show_project, show_galleries_popup, add_contract_to_project

app_name = "investments"
urlpatterns = [
    path("list/", investment_projects_list, name="investment_projects_list"),
    path("new/", add_new_project, name="add_new_project"),
    re_path("edit/(?P<id>\d+)/$", edit_project, name="edit_project"),
    re_path("show/(?P<id>\d+)/$", show_project, name="show_project"),
    re_path("gallery/(?P<id>\d+)/$", show_galleries_popup, name="show_galleries_popup"),
    re_path("addToProject/(?P<id>\d+)/$", add_contract_to_project, name="add_contract_to_project"),
    path("", make_important_task_investments, name="make_important_task_investments")

]
