import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from gallery.models import Gallery, Photo
from gallery.forms import GalleryForm, PhotoForm

logger = logging.getLogger(__name__)


# Create your views here.
class GalleryListView(LoginRequiredMixin, View):
    template = "gallery/galleries.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            galleries = Gallery.objects.all()
            gallery_count = len(galleries)
            context = {'galleries': galleries,
                       'gallery_count': gallery_count}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddGallery(LoginRequiredMixin, View):
    template = "gallery/gallery_form.html"
    redirect = 'gallery:new_gallery_details'
    template_error = 'main/error_site.html'
    form_class = GalleryForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'gallery_form': form}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None)

            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.author = request.user
                    form.save()
                    return redirect(self.redirect, instance.id)
            context = {'gallery_form': form}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class GalleryDetailsView(LoginRequiredMixin, View):
    template = "gallery/gallery.html"
    template_error = 'main/error_site.html'
    redirect = "gallery:gallery_details"
    form_class = PhotoForm

    def get(self, request, gallery_id):
        try:
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
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, gallery_id):
        try:
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
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewGalleryDetails(LoginRequiredMixin, View):
    template = "gallery/new_gallery.html"
    template_error = 'main/error_site.html'
    redirect = "gallery:new_gallery_details"
    form_class = PhotoForm

    def get(self, request, gallery_id):
        try:
            gallery = Gallery.objects.get(pk=gallery_id)
            photos = gallery.photo.all()
            photocount = len(photos)
            photo_form = PhotoForm()
            context = {'gallery': gallery, 'photocount': photocount, 'photo_form': photo_form}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, gallery_id):
        try:
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
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
