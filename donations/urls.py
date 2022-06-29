from django.urls import path
from donations.views import donations_list

app_name = 'donations'

urlpatterns = [
    path('darowizny/', donations_list, name='donations_list')
]