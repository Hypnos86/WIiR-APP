from django.urls import path
from gallery.views import gallery_details, gallery_list, add_gallery, new_gallery_details

app_name = 'gallery'

urlpatterns = [
    path('galleries/', gallery_list, name='gallery_list'),
    path('newGallery/', add_gallery, name='add_gallery'),
    path('galleryDetails/<int:gallery_id>/', gallery_details, name='gallery_details'),
    path('gallery/<int:gallery_id>/', new_gallery_details, name='new_gallery_details')
]
