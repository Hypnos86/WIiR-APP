from django.forms import ModelForm, ModelMultipleChoiceField, DateInput, Textarea
from investments.models import Project
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.contrib import admin
from main.models import Employer


class DataFiled(DateInput):
    input_type = 'date'


class ProjectForm(ModelForm):
    worker = ModelMultipleChoiceField(queryset=Employer.objects.all(),
                                      widget=AutocompleteSelectMultiple(Project._meta.get_field('worker'),
                                                                        admin.AdminSite(), ))

    class Meta:
        model = Project
        fields = ['date_of_acceptance', 'no_acceptance_document', 'investment_program', 'project_title',
                  'investment_cost_estimate_value', 'unit', 'section', 'group', 'paragraph',
                  'source_financing', 'information', 'date_of_settlement', 'settlement_scan', 'realized', 'worker',
                  'creation_date', 'change', 'author']

        label = {'date_of_acceptance': 'Data akceptacji programu',
                 'no_acceptance_document': 'L.dz.',
                 'investment_program': 'Program inwestycyjny',
                 'project_title': 'Tytuł zadania',
                 'investment_cost_estimate_value': 'Wartość kosztorysowa zadania',
                 'unit': 'Jednostka',
                 'section': 'Rozdział',
                 'group': 'Grupa',
                 'paragraph': 'Paragraf',
                 'source_financing': 'Źródło finansowania',
                 'information': 'Informacje',
                 'date_of_settlement': 'Data rozliczenia',
                 'settlement_scan': 'Skan rozliczenia',
                 'realized': 'Zrealizowano',
                 'worker': 'Pracownik',
                 'creation_date': 'Data utworzenia',
                 'change': 'Zmiany',
                 'author': 'Autor'}
        exclude = ['creation_date', 'change', 'author']
        widgets = {
            'date_of_acceptance': DataFiled(),
            'date_of_settlement': DataFiled(),
            'source_financing': Textarea(attrs={'rows': 3}),
            'information': Textarea(attrs={'rows': 3})
        }
