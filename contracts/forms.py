from django.forms import ModelForm
from contracts.models import Contractimmovables, Stan, Rodzaj, Podstawa


class ContractimmovablesForm(ModelForm):
    class Meta:
        name = Contractimmovables
        field = ['data_umowy', 'nrumowy', 'kontrahent', 'podstawa', 'okres_obowiazywania', 'rodzaj', 'pow_uzyczona',
                 'koszt_czynsz', 'koszt_prad', 'koszt_gaz',  'koszt_woda',  'koszt_co', 'koszt_smieci',
                 'unit', 'skan', 'stan', 'comments', 'archives', 'create', 'change', 'autor']
        labels = {'data_umowy': 'Data umowy', 'nrumowy': 'Nr umowy', 'kontrahent': 'Kontrahent',
                  'podstawa': 'Podstawa prawda', 'okres_obowiazywania': 'Okres obowiązywania', 'rodzaj': 'Rodzaj umowy',
                  'pow_uzyczona': 'Powiezchnia użytkowa', 'koszt_czynsz': 'Czynsz',
                  'koszt_prad': 'Prąd', 'koszt_gaz': 'Gaz', 'koszt_woda': 'Woda', 'koszt_co': 'C.O.', 'koszt_smieci': 'Śmieci',
                  'unit': 'Jednostka', 'skan': 'Skan umowy', 'stan': 'Stan umowy', 'comments': 'Uwagi',
                  'archives': 'Archiwum', 'create': 'Utworzenie', 'change': 'Zmiany', 'autor': 'Autor'}
