from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from sourcefinancing.models import Section, Group, Paragraph, Source, Financesource

# Register your models here.
admin.site.register(Section)
admin.site.register(Group)
admin.site.register(Paragraph)
admin.site.register(Source)


class FinancesourceResource(resources.ModelResource):
    section = Field(attribute='section', column_name='Rozdział')
    group = Field(attribute='group', column_name='Grupa')
    paragraph = Field(attribute='paragraph', column_name='Paragraf')
    source = Field(attribute='source', column_name='Źródło')

    class Meta:
        model = Financesource
        # fields = ('id',)
        export_order = ('section', 'group', 'paragraph', 'source')
        exclude = ('id')


@admin.register(Financesource)
class UnitAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['section', 'group', 'paragraph', 'source']
    ordering = ['section', 'group', 'paragraph', 'source']
    list_filter = ['section', 'paragraph']
    resource_class = FinancesourceResource
