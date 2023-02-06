from django.urls import path
from main.views import make_list_register, welcome, make_secretariat_site, show_employers_list, show_command_list, \
    give_access_to_modules, telephone_list, show_teams_list, add_team_popup, edit_team_popup, \
    add_employer_popup, edit_employer_popup, add_command_popup, edit_command_popup, delete_command_popup, \
    add_secretariat_number, edit_secretariat_number, delete_secretariat_number, edit_rent_car, delete_rent_car, add_rent_car

app_name = 'main'
urlpatterns = [
    path('secretariat/', make_secretariat_site, name='make_secretariat_site'),
    path('addRentCar/', add_rent_car, name='add_rent_car'),
    path('rentCar/<int:id>/', edit_rent_car, name='edit_rent_car'),
    path('deleteRentCar/<int:id>/', delete_rent_car, name='delete_rent_car'),
    path('addSecretariatInfo/', add_secretariat_number, name='add_secretariat_number'),
    path('editSecretariatInfo/<int:id>/', edit_secretariat_number, name='edit_secretariat_number'),
    path('delete_secretariat/<int:id>/', delete_secretariat_number, name='delete_secretariat_number'),
    path('teams/', show_teams_list, name='show_teams_list'),
    path('addTeam/', add_team_popup, name='add_team_popup'),
    path('editTeam/<int:id>/', edit_team_popup, name='edit_team_popup'),
    path('employers/', show_employers_list, name='show_employers_list'),
    path('addEmployers/', add_employer_popup, name='add_employer_popup'),
    path('editEmployers/<int:id>/', edit_employer_popup, name='edit_employer_popup'),
    path('commands/', show_command_list, name='show_command_list'),
    path('addCommands/', add_command_popup, name='add_command_popup'),
    path('editCommands/<int:id>/', edit_command_popup, name='edit_command_popup'),
    path('deleteCommands/<int:id>/', delete_command_popup, name='delete_command_popup'),
    path('access/', give_access_to_modules, name='give_access_to_modules'),
    path('registerList/', make_list_register, name='make_list_register'),
    path('telephones/', telephone_list, name='telephone_list'),
    path('', welcome, name='welcome')
]
