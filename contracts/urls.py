from django.urls import path
from contracts.views import menu_contractsimmovables, new_contractsimmovables, edit_contractsimmovables, show_contractsimmovables

app_name = 'contracts'
urlpatterns = [
    path('', menu_contractsimmovables, name='menu_contractsimmovables'),
    path('newcontractimmovables/', new_contractsimmovables, name='new_contractsimmovables'),
    path('editcontractimmovables/<int:id>', edit_contractsimmovables, name='edit_contractsimmovables'),
    path('showcontractimmovables/<int:id>', show_contractsimmovables, name='show_contractsimmovables')
]
