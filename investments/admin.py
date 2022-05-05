from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from investments.models import Project

# Register your models here.
admin.site.register(Project)
