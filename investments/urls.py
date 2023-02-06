from django.urls import path
from investments.views import make_important_task_investments, investment_projects_list, add_new_project, edit_project, \
    show_project, show_galleries_popup, add_contract_to_project

app_name = "investments"
urlpatterns = [
    path("investments/", investment_projects_list, name="investment_projects_list"),
    path("newInvestments/", add_new_project, name="add_new_project"),
    path("editInvestment/<int:id>/", edit_project, name="edit_project"),
    path("showInvestment/<int:id>/", show_project, name="show_project"),
    path("projectGallery/<int:id>/", show_galleries_popup, name="show_galleries_popup"),
    path("addContractToProject/<int:id>/", add_contract_to_project, name="add_contract_to_project"),
    path("", make_important_task_investments, name="make_important_task_investments")

]
