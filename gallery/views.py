from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from gallery.models import Gallery, Photo
from gallery.forms import GalleryForm, PhotoForm


# Create your views here.
class GalleryListView(LoginRequiredMixin, View):
    template = "gallery/galleries.html"

    def get(self, request):
        galleries = Gallery.objects.all()
        gallery_count = len(galleries)
        context = {'galleries': galleries,
                   'gallery_count': gallery_count}
        return render(request, self.template, context)


@login_required
def add_gallery(request):
    gallery_form = GalleryForm(request.POST or None)
    context = {'gallery_form': gallery_form}

    if request.method == 'POST':
        if gallery_form.is_valid():
            instance = gallery_form.save(commit=False)
            instance.author = request.user
            gallery_form.save()
            return redirect('gallery:new_gallery_details', instance.id)
    return render(request, 'gallery/gallery_form.html', context)


class GalleryDetailsView(LoginRequiredMixin, View):
    template = "gallery/gallery.html"
    redirect = "gallery:gallery_details"

    def get(self, request, gallery_id):
        gallery = Gallery.objects.get(pk=gallery_id)
        photos = gallery.photo.all()
        photocount = len(photos)
        photo_form = PhotoForm()

        if request.method == 'POST':
            photo_list_post = request.FILES.getlist('images')
            for img in photo_list_post:
                instance = Photo.objects.create(src=img, gallery=gallery)
                instance.save()
            return redirect(self.redirect, gallery.id)
        context = {'gallery': gallery, 'photocount': photocount, 'photo_form': photo_form}
        return render(request, self.template, context)


# class NewGalleryDetails(LoginRequiredMixin, View):
#     template = "gallery/new_gallery.html"
#     redirect = "gallery:new_gallery_details"

@login_required
def new_gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    photos = gallery.photo.all()
    photocount = len(photos)
    photo_form = PhotoForm()

    if request.method == 'POST':
        photo_list_post = request.FILES.getlist('images')
        for img in photo_list_post:
            instance = Photo.objects.create(src=img, gallery=gallery)
            instance.save()
        return redirect('gallery:new_gallery_details', gallery.id)
    context = {'gallery': gallery, 'photocount': photocount, 'photo_form': photo_form}
    return render(request, 'gallery/new_gallery.html', context)
