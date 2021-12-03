from django.forms import ModelForm
from contracts.models import Contract, Stan, Rodzaj, Podstawa


class ContractForm(ModelForm):
    class Meta:
        name = Contract
        field = ['data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj', 'pow_uzyczona',
                 'koszt_prad', 'inf_prad', 'koszt_gaz', 'inf_gaz', 'koszt_woda', 'inf_woda', 'koszt_co', 'inf_co',
                 'unit', 'skan', 'stan', 'comments', 'archives', 'create', 'change', 'autor']
        labels = {'data_umowy': 'Data umowy', 'nrumowy': 'Nr umowy', 'kontrahent': 'Kontrahent',
                  'podstawa': 'Podstawa prawda', 'okres_obowiazywania': 'Okres obowiązywania', 'rodzaj': 'Rodzaj umowy',
                  'pow_uzyczona': 'Powiezchnia użytkowa',
                  'koszt_prad': 'Prąd',
                  'inf_prad': 'Informacje', 'koszt_gaz': 'Gaz', 'inf_gaz': 'Informacje', 'koszt_woda': 'Woda',
                  'inf_woda': 'Informacje', 'koszt_co': 'C.O.', 'inf_co': 'Informacje',
                  'unit': 'Jednostka', 'skan': 'Skan umowy', 'stan': 'Stan umowy', 'comments': 'Uwagi',
                  'archives': 'Archiwóm', 'create': 'Utworzenie', 'change': 'Zmiany', 'autor': 'Autor'}
