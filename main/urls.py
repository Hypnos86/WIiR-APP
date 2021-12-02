from django.urls import path
from main.views import telephone_list

app_name = 'main'
urlpatterns = [
    path('telephones/', telephone_list,  name='telephone_list')
]
