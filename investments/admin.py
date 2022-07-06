from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ManyToManyWidget
from import_export.admin import ExportMixin
from import_export.fields import Field
from investments.models import Project


# Register your models here.
class ProjectResources(resources.ModelResource):
    date_of_acceptance = Field(attribute='date_of_acceptance', column_name='Data akceptacji')
    no_acceptance_document = Field(attribute='no_acceptance_document', column_name='L.dz. dokumentu')
    project_title = Field(attribute='project_title', column_name='Nazwa zadania')
    investment_cost_estimate_value = Field(attribute='investment_cost_estimate_value', column_name='WKI')
    unit = Field(attribute='unit', column_name='Jednostka')
    section = Field(attribute='section', column_name='Rozdział')
    group = Field(attribute='group', column_name='Grupa')
    paragraph = Field(attribute='paragraph', column_name='Paragraf')
    source_financing = Field(attribute='source_financing', column_name='Źrudło finansowania')
    information = Field(attribute='information', column_name='Informacje')
    date_of_settlement = Field(attribute='date_of_settlement', column_name='Data rozliczenia')
    realized = Field(attribute='realized', column_name='Zrealizowane')
    worker = fields.Field(attribute='worker', column_name='Odpowiedzialny',
                          widget=ManyToManyWidget(Project, separator=',', field='last_name'))

    class Meta:
        model = Project
        fields = ('date_of_acceptance', 'no_acceptance_document', 'project_title',
                  'investment_cost_estimate_value', 'unit', 'section', 'group', 'paragraph',
                  'source_financing', 'information', 'date_of_settlement', 'worker', 'realized',)
        export_order = ('date_of_acceptance', 'no_acceptance_document', 'unit', 'project_title',
                        'investment_cost_estimate_value', 'section', 'group', 'paragraph',
                        'source_financing', 'information', 'date_of_settlement', 'worker', 'realized',)


@admin.register(Project)
class ProjectAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['date_of_acceptance', 'project_title', 'investment_cost_estimate_value', 'unit', 'realized', 'creation_date', 'change', 'author']
    list_display_links = ['project_title']
    autocomplete_fields = ('worker',)
    resource_class = ProjectResources
