from django.contrib import admin
from gallery.models import Gallery, Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallery', 'add_date']
    search_fields = ['gallery__project__project_title', 'gallery__project__unit__city']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'add_date', 'author']
    list_display_links = ('name',)
    search_fields = ['project__project_title', 'project__unit__city']
