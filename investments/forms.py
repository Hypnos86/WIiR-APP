from django.forms import ModelForm, ModelMultipleChoiceField, DateInput, Textarea
from main.forms import DateField
from investments.models import Project
from tinymce.widgets import TinyMCE
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.contrib import admin
from main.models import Employer


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['date_of_acceptance', 'no_acceptance_document', 'investment_program', 'project_title',
                  'investment_cost_estimate_value', 'unit', 'section', 'group', 'paragraph',
                  'source_financing', 'information', 'date_of_settlement', 'settlement_scan', 'realized', 'worker',
                  'creation_date', 'change', 'author']

        labels = {'date_of_acceptance': 'Data akceptacji programu',
                  'no_acceptance_document': 'L.dz.',
                  'investment_program': 'Program inwestycyjny',
                  'project_title': 'Tytuł zadania',
                  'investment_cost_estimate_value': 'WKI',
                  'unit': 'Jednostka',
                  'section': 'Rozdział',
                  'group': 'Grupa',
                  'paragraph': 'Paragraf',
                  'source_financing': 'Opis źródła finansowania',
                  'information': 'Informacje',
                  'date_of_settlement': 'Data rozliczenia',
                  'settlement_scan': 'Skan rozliczenia',
                  'realized': 'Zrealizowano',
                  'worker': 'Branżysta',
                  'creation_date': 'Data utworzenia',
                  'change': 'Zmiany',
                  'author': 'Autor'}
        exclude = ['creation_date', 'change', 'author']
        widgets = {
            'date_of_acceptance': DateField(),
            'date_of_settlement': DateField(),
            'source_financing': TinyMCE(attrs={'cols': 5, 'rows': 3}),
            'information': TinyMCE(attrs={'cols': 5, 'rows': 3})
        }
