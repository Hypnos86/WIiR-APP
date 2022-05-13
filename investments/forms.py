from django.forms import ModelForm
from investments.models import Project


class ProjectForm(ModelForm):
    model = Project
    fields = ['date_of_acceptance', 'no_acceptance_document', 'investment_program', 'project_title',
              'investment_cost_estimate_value', 'unit', 'section', 'group', 'paragraph', 'paragraph',
              'source_financing', 'information', 'date_of_settlement', 'settlement_scan', 'realized', 'creation_date',
              'change']
    label = {'date_of_acceptance': 'Data akceptacji', 'no_acceptance_document': 'L.dz.',
             'investment_program': 'Program inwestycyjny', 'project_title': 'Tytuł zadania',
             'investment_cost_estimate_value': 'Wartość kosztorysowa zadania', 'unit': 'Jednostka',
             'section': 'Rozdział', 'group': 'Grupa', 'paragraph': 'Paragraf',
             'source_financing': 'Źródło finansowania', 'information': 'Informacje',
             'date_of_settlement': 'Data rozliczenia', 'settlement_scan': 'Skan rozliczenia',
             'realized': 'Zrealizowano',
             'change': 'Zmiany'}
    exclude = ['author']
