from django.urls import path
from .views import make_contractor_list, make_new_contractor, edit_contractor

app_name = 'contractors'
urlpatterns = [
    path('newcontractor/', make_new_contractor, name="contractorform"),
    path('editcontractor/<int:id>', edit_contractor, name="editcontractor"),
    path('', make_contractor_list, name='contractorlist')

]
