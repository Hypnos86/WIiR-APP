from django.urls import path
from main.views import make_list_register, welcome, give_access_to_modules, make_command_list, telephone_list

app_name = 'main'
urlpatterns = [
    path('access/', give_access_to_modules, name='give_access_to_modules'),
    path('command/', make_command_list, name='make_command_list'),
    path('ewidencja/', make_list_register, name='make_list_register'),
    path('telephones/', telephone_list, name='telephone_list'),
    path('', welcome, name='welcome')
]
