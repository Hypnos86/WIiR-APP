from django.urls import path
from gallery.views import gallery_details

app_name = 'gallery'

urlpatterns = [
    path('galeria/<int:gallery_id>/', gallery_details, name='gallery_details')
]
