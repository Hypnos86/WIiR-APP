from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from gallery.models import Gallery, Photo
from gallery.forms import GalleryForm, PhotoForm


# Create your views here.
@login_required
def gallery_list(request):
    galleries = Gallery.objects.all()
    gallery_count = len(galleries)
    context = {'galleries': galleries,
               'gallery_count': gallery_count}
    return render(request, 'gallery/galleries.html', context)


@login_required
def add_gallery(request):
    gallery_form = GalleryForm(request.POST or None)
    context = {'gallery_form': gallery_form}

    if request.method == 'POST':
        if gallery_form.is_valid():
            instance = gallery_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('gallery:gallery_list')
    return render(request, 'gallery/gallery_form.html', context)


@login_required
def gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    photos = gallery.photo.all()
    photocount = len(photos)
    return render(request, 'gallery/gallery.html', {'gallery': gallery, 'photocount': photocount})


@login_required
def add_photo_to_gallery(request, id):
    gallery = Gallery.objects.get(pk=id)
    photo = PhotoForm()
    context = {'gallery': gallery,
               'photo': photo}
    return render(request, 'gallery/add_photo.html', context)
