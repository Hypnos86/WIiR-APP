from django.urls import path
from .views import make_list_register

app_name = 'listregister'
urlpatterns = [
    path('', make_list_register, name='make_list_register')
]
