from django.urls import path
from gallery.views import gallery_details, gallery_list, add_gallery, new_gallery_details

app_name = 'gallery'

urlpatterns = [
    path('galerie/', gallery_list, name='gallery_list'),
    path('nowa_galeria/', add_gallery, name='add_gallery'),
    path('galeria/<int:gallery_id>/', gallery_details, name='gallery_details'),
    path('galeria/<int:gallery_id>/', new_gallery_details, name='new_gallery_details')
]
