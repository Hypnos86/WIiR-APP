from django.urls import path
from .views import contractor_list, make_new_contractor, edit_contractor

app_name = 'contractors'
urlpatterns = [
    path('', contractor_list, name="contractorlist"),
    path('newcontractor/', make_new_contractor, name="contractorform"),
    path('editcontractor/<int:id>', edit_contractor, name="editcontractor"),

]
