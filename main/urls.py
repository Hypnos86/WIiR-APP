from django.urls import path
from main.views import telephone_list, welcome, give_access_to_modules, make_command_list

app_name = 'main'
urlpatterns = [
    path('telephones/', telephone_list, name='telephone_list'),
    path('access/', give_access_to_modules, name='give_access_to_modules'),
    path('command/', make_command_list, name='make_command_list'),
    path('', welcome, name='welcome')
]
