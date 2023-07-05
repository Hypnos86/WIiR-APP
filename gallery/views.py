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


class AddGallery(LoginRequiredMixin, View):
    template = "gallery/gallery_form.html"
    redirect = 'gallery:new_gallery_details'
    form_class = GalleryForm

    def get(self, request):
        form = self.form_class()
        context = {'gallery_form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form_class(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect(self.redirect, instance.id)
        context = {'gallery_form': form}
        return render(request, self.template, context)


class GalleryDetailsView(LoginRequiredMixin, View):
    template = "gallery/gallery.html"
    redirect = "gallery:gallery_details"
    form_class = PhotoForm

    def get(self, request, gallery_id):
        gallery = Gallery.objects.get(pk=gallery_id)
        photos = gallery.photo.all()
        photocount = len(photos)
        form = self.form_class()

        if request.method == 'POST':
            photo_list_post = request.FILES.getlist('images')
            for img in photo_list_post:
                instance = Photo.objects.create(src=img, gallery=gallery)
                instance.save()
            return redirect(self.redirect, gallery.id)
        context = {'gallery': gallery, 'photocount': photocount, 'photo_form': form}
        return render(request, self.template, context)

    def post(self, request, gallery_id):
        gallery = Gallery.objects.get(pk=gallery_id)
        photos = gallery.photo.all()
        photocount = len(photos)
        form = self.form_class()

        if request.method == 'POST':
            photo_list_post = request.FILES.getlist('images')
            for img in photo_list_post:
                instance = Photo.objects.create(src=img, gallery=gallery)
                instance.save()
            return redirect(self.redirect, gallery.id)
        context = {'gallery': gallery, 'photocount': photocount, 'photo_form': form}
        return render(request, self.template, context)


class NewGalleryDetails(LoginRequiredMixin, View):
    template = "gallery/new_gallery.html"
    redirect = "gallery:new_gallery_details"
    form_class = PhotoForm

    def get(self, request, gallery_id):
        gallery = Gallery.objects.get(pk=gallery_id)
        photos = gallery.photo.all()
        photocount = len(photos)
        photo_form = PhotoForm()
        context = {'gallery': gallery, 'photocount': photocount, 'photo_form': photo_form}
        return render(request, self.template, context)

    def post(self, request, gallery_id):
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
