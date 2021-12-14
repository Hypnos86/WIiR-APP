from django.urls import path
from cpvdict.views import cpvlist

app_name = 'cpvdict'
urlpatterns = [
    path('slownikcpv/', cpvlist, name='cpvlist')
]
