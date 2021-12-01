from django.urls import path
from .views import contractor_list, new_contractor, edit_contractor

app_name = 'contractors'
urlpatterns = [
    path('newcontractor/', new_contractor, name="new_contractor"),
    path('editcontractor/<int:id>', edit_contractor, name="edit_contractor"),
    path('', contractor_list, name="contractor_list"),

]
