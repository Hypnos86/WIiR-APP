from django.shortcuts import render
from gallery.models import Gallery, Photo


# Create your views here.
def gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    photos = gallery.photo.all()
    photocount = len(photos)
    return render(request, 'gallery/gallery.html', {'gallery': gallery, 'photocount': photocount})
