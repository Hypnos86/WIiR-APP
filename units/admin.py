from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Powiat, Rodzaj, Jednostka


# admin.site.register(Post, PostAdmin)
class PostResource(resources.ModelResource):
    class Meta:
        model = Powiat,
        model = Jednostka


@admin.register(Powiat)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', "powiat"]
    resource_class = PostResource


admin.site.register(Rodzaj)


@admin.register(Jednostka)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'powiat', 'rodzaj', 'adres', 'kod_pocztowy', 'miasto', 'aktywna']
    search_fields = ['adres, miasto']
    list_filter = ['powiat']
    resource_class = PostResource
