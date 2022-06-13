from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
            return redirect('gallery:gallery_details', instance.id)
    return render(request, 'gallery/gallery_form.html', context)


@login_required
def gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    photos = gallery.photo.all()
    photocount = len(photos)
    photo_form = PhotoForm()

    if request.method == 'POST':
        photo_form = request.FILES.getlist('images')
        for img in photo_form:
            instance = photos.objects.create(photo_form=img)
            instance.save(commit=False)
            instance.gallery = gallery
            instance.save()
        return redirect('gallery:gallery_details', gallery.id)

    return render(request, 'gallery/gallery.html',
                  {'gallery': gallery, 'photocount': photocount, 'photo_form': photo_form})
