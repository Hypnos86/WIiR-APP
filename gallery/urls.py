from django.urls import path, re_path
from gallery.views import GalleryDetailsView, GalleryListView, AddGallery, NewGalleryDetails

app_name = 'gallery'

urlpatterns = [
    path('all/', GalleryListView.as_view(), name='gallery_list'),
    path('new/', AddGallery.as_view(), name='add_gallery'),
    re_path('details/(?P<gallery_id>\d+)/$', GalleryDetailsView.as_view(), name='gallery_details'),
    re_path('(?P<gallery_id>\d+)/$', NewGalleryDetails.as_view(), name='new_gallery_details')
]
