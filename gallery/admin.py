from django.contrib import admin
from gallery.models import Gallery, Photo

# Register your models here.

admin.site.register(Photo)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'add_date', 'author']
    list_display_links = ('name',)
    search_fields = ['project__project_title']