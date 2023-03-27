from django.urls import path, re_path
from gallery.views import gallery_details, gallery_list, add_gallery, new_gallery_details

app_name = 'gallery'

urlpatterns = [
    path('all/', gallery_list, name='gallery_list'),
    path('new/', add_gallery, name='add_gallery'),
    re_path('details/(?P<gallery_id>\d+)/$', gallery_details, name='gallery_details'),
    re_path('(?P<gallery_id>\d+)/$', new_gallery_details, name='new_gallery_details')
]
