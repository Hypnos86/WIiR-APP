from django.urls import path
from main.views import make_list_register, welcome, make_secretariat_site, show_employers_list, show_command_list, \
    give_access_to_modules, telephone_list, show_teams_list, add_team_popup, edit_team_popup, \
    add_employer_popup, edit_employer_popup, add_command_popup, edit_command_popup, delete_command_popup, \
    add_secretariat_number, edit_secretariat_number, delete_secretariat_number

app_name = 'main'
urlpatterns = [
    path('secretariat/', make_secretariat_site, name='make_secretariat_site'),
    path('add_secretariat', add_secretariat_number, name='add_secretariat_number'),
    path('edit_secretariat/<int:id>', edit_secretariat_number, name='edit_secretariat_number'),
    path('delete_secretariat/<int:id>', delete_secretariat_number, name='delete_secretariat_number'),
    path('teams/', show_teams_list, name='show_teams_list'),
    path('add_team/', add_team_popup, name='add_team_popup'),
    path('edit_team/<int:id>', edit_team_popup, name='edit_team_popup'),
    path('employers/', show_employers_list, name='show_employers_list'),
    path('add_employers/', add_employer_popup, name='add_employer_popup'),
    path('edit_employers/<int:id>', edit_employer_popup, name='edit_employer_popup'),
    path('commands/', show_command_list, name='show_command_list'),
    path('add_commands/', add_command_popup, name='add_command_popup'),
    path('edit_commands/<int:id>', edit_command_popup, name='edit_command_popup'),
    path('delete_commands/<int:id>', delete_command_popup, name='delete_command_popup'),
    path('access/', give_access_to_modules, name='give_access_to_modules'),
    path('register_list/', make_list_register, name='make_list_register'),
    path('telephones/', telephone_list, name='telephone_list'),
    path('', welcome, name='welcome')
]
