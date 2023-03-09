from django.urls import path, re_path
from main.views import ListRegisterView, WelcomeView, SecretariatSiteView, EmployersListView, CommandListView, \
    AccessToModulesView, TelephoneListView, ShowTeamsListView, NewTeamView, EditTeamView, \
    NewEmployerView, EditEmployerView, AddCommandView, EditCommandView, DeleteCommandView, \
    NewSecretariatNumberView, EditSecretariatNumberView, DeleteSecretariatNumberView, EditRentCarView, DeleteRentCar, \
    NewRentCatView

app_name = 'main'
urlpatterns = [
    path('secretariat/', SecretariatSiteView.as_view(), name='make_secretariat_site'),
    path('addRentCar/', NewRentCatView.as_view(), name='add_rent_car'),
    re_path('rentCar/(?P<id>\d+)/$', EditRentCarView.as_view(), name='edit_rent_car'),
    re_path('deleteRentCar/(?P<id>\d+)/$', DeleteRentCar.as_view(), name='delete_rent_car'),
    path('addSecretariatInfo/', NewSecretariatNumberView.as_view(), name='add_secretariat_number'),
    re_path('editSecretariatInfo/(?P<id>\d+)/$', EditSecretariatNumberView.as_view(), name='edit_secretariat_number'),
    re_path('delete_secretariat/(?P<id>\d+)/$', DeleteSecretariatNumberView.as_view(), name='delete_secretariat_number'),
    path('teams/', ShowTeamsListView.as_view(), name='show_teams_list'),
    path('addTeam/', NewTeamView.as_view(), name='add_team_popup'),
    re_path('editTeam/(?P<id>\d+)/$', EditTeamView.as_view(), name='edit_team_popup'),
    path('employers/', EmployersListView.as_view(), name='show_employers_list'),
    path('addEmployers/', NewEmployerView.as_view(), name='add_employer_popup'),
    re_path('editEmployers/(?P<id>\d+)/$', EditEmployerView.as_view(), name='edit_employer_popup'),
    path('commands/', CommandListView.as_view(), name='show_command_list'),
    path('addCommands/', AddCommandView.as_view(), name='add_command_popup'),
    re_path('editCommands/(?P<id>\d+)/$', EditCommandView.as_view(), name='edit_command_popup'),
    re_path('deleteCommands/(?P<id>\d+)/$', DeleteCommandView.as_view(), name='delete_command_popup'),
    path('access/', AccessToModulesView.as_view(), name='give_access_to_modules'),
    path('registerList/', ListRegisterView.as_view(), name='make_list_register'),
    path('telephones/', TelephoneListView.as_view(), name='telephone_list'),
    path('', WelcomeView.as_view(), name='welcome')
]
