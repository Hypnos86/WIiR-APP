from django.urls import path
from main.views import make_list_register, welcome, make_secretariat_site, show_employers_list, show_command_list, \
    give_access_to_modules, show_command, telephone_list, show_teams_list, add_team_popup, edit_team_popup, \
    add_employer_popup, edit_employer_popup, add_command_popup

app_name = 'main'
urlpatterns = [
    path('secretariat/', make_secretariat_site, name='make_secretariat_site'),
    path('teams/', show_teams_list, name='show_teams_list'),
    path('add_team/', add_team_popup, name='add_team_popup'),
    path('edit_team/<int:id>', edit_team_popup, name='edit_team_popup'),
    path('employers/', show_employers_list, name='show_employers_list'),
    path('add_employers/', add_employer_popup, name='add_employer_popup'),
    path('edit_employers/<int:id>', edit_employer_popup, name='edit_employer_popup'),
    path('commands/', show_command_list, name='show_command_list'),
    path('add_commands/', add_command_popup, name='add_command_popup'),
    path('access/', give_access_to_modules, name='give_access_to_modules'),
    path('command/', show_command, name='show_command'),
    path('rgister_list/', make_list_register, name='make_list_register'),
    path('telephones/', telephone_list, name='telephone_list'),
    path('', welcome, name='welcome')
]
