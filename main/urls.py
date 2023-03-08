from django.urls import path, re_path
from main.views import ListRegisterView, WelcomeView, SecretariatSiteView, EmployersListView, show_command_list, \
    AccessToModulesView, TelephoneListView, ShowTeamsListView, NewTeamView, EditTeam, \
    NewEmployerView, edit_employer_popup, add_command_popup, edit_command_popup, delete_command_popup, \
    NewSecretariatNumberView, edit_secretariat_number, delete_secretariat_number, EditRentCarView, delete_rent_car, \
    NewRentCatView

app_name = 'main'
urlpatterns = [
    path('secretariat/', SecretariatSiteView.as_view(), name='make_secretariat_site'),
    path('addRentCar/', NewRentCatView.as_view(), name='add_rent_car'),
    re_path('rentCar/(?P<id>\d+)/$', EditRentCarView.as_view(), name='edit_rent_car'),
    re_path('deleteRentCar/(?P<id>\d+)/$', delete_rent_car, name='delete_rent_car'),
    path('addSecretariatInfo/', NewSecretariatNumberView.as_view(), name='add_secretariat_number'),
    re_path('editSecretariatInfo/(?P<id>\d+)/$', edit_secretariat_number, name='edit_secretariat_number'),
    re_path('delete_secretariat/(?P<id>\d+)/$', delete_secretariat_number, name='delete_secretariat_number'),
    path('teams/', ShowTeamsListView.as_view(), name='show_teams_list'),
    path('addTeam/', NewTeamView.as_view(), name='add_team_popup'),
    re_path('editTeam/(?P<id>\d+)/$', EditTeam.as_view(), name='edit_team_popup'),
    path('employers/', EmployersListView.as_view(), name='show_employers_list'),
    path('addEmployers/', NewEmployerView.as_view(), name='add_employer_popup'),
    re_path('editEmployers/(?P<id>\d+)/$', edit_employer_popup, name='edit_employer_popup'),
    path('commands/', show_command_list, name='show_command_list'),
    path('addCommands/', add_command_popup, name='add_command_popup'),
    re_path('editCommands/(?P<id>\d+)/$', edit_command_popup, name='edit_command_popup'),
    re_path('deleteCommands/(?P<id>\d+)/$', delete_command_popup, name='delete_command_popup'),
    path('access/', AccessToModulesView.as_view(), name='give_access_to_modules'),
    path('registerList/', ListRegisterView.as_view(), name='make_list_register'),
    path('telephones/', TelephoneListView.as_view(), name='telephone_list'),
    path('', WelcomeView.as_view(), name='welcome')
]
