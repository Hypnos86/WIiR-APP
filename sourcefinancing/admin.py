from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from sourcefinancing.models import Section, Group, Paragraph, Source, FinanceSource

# Register your models here.
admin.site.register(Section)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group', 'name']
    

admin.site.register(Paragraph)
admin.site.register(Source)


class FinanceSourceResource(resources.ModelResource):
    section = Field(attribute='section', column_name='Rozdział')
    group = Field(attribute='group', column_name='Grupa')
    paragraph = Field(attribute='paragraph', column_name='Paragraf')
    source = Field(attribute='source', column_name='Źródło')

    class Meta:
        model = FinanceSource
        # fields = ('id',)
        export_order = ('section', 'group', 'paragraph', 'source')
        exclude = ('id')


@admin.register(FinanceSource)
class UnitAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['section', 'group', 'paragraph', 'source']
    ordering = ['section', 'group', 'paragraph', 'source']
    list_filter = ['section', 'paragraph']
    resource_class = FinanceSourceResource
