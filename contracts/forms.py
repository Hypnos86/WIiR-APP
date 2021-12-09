from django.forms import ModelForm, DateInput, Textarea
from contracts.models import Contractimmovables


class DateField(DateInput):
    input_type = "date"


class ContractimmovablesForm(ModelForm):
    class Meta:
        model = Contractimmovables
        fields = ['data_umowy', 'nrumowy', 'kontrahent', 'okres_obowiazywania', 'pow_uzyczona', 'podstawa',
                 'rodzaj', 'koszt_czynsz', 'koszt_prad', 'koszt_gaz', 'koszt_woda', 'koszt_co', 'koszt_smieci',
                 'koszt_podsmiec', 'koszt_podnier', 'unit', 'skan', 'stan', 'comments', 'archives', 'create',
                 'change', 'autor']

        field_order = ['data_umowy', 'nrumowy', 'kontrahent', 'okres_obowiazywania', 'pow_uzyczona', 'podstawa',
                       'rodzaj', 'koszt_czynsz', 'koszt_prad', 'koszt_gaz', 'koszt_woda', 'koszt_co', 'koszt_smieci',
                       'koszt_podsmiec', 'koszt_podnier', 'unit', 'skan', 'stan', 'comments', 'archives', 'create',
                       'change', 'autor']

        labels = {'data_umowy': 'Data umowy', 'nrumowy': 'Nr umowy', 'kontrahent': 'Kontrahent',
                  'podstawa': 'Podstawa prawda', 'okres_obowiazywania': 'Okres obowiązywania', 'rodzaj': 'Rodzaj umowy',
                  'pow_uzyczona': 'Powiezchnia użytkowa', 'koszt_czynsz': 'Czynsz',
                  'koszt_prad': 'Prąd', 'koszt_gaz': 'Gaz', 'koszt_woda': 'Woda', 'koszt_co': 'C.O.',
                  'koszt_smieci': 'Śmieci',
                  'koszt_podsmiec': 'Zagospodarowanie odpadami komunalnymi',
                  'koszt_podnier': 'Podatek od nieruchomości',
                  'unit': 'Jednostka', 'skan': 'Skan umowy', 'stan': 'Stan umowy', 'comments': 'Informacje'}

        exclude = ['archives', 'create', 'change', 'autor']

        widgets = {'data_umowy': DateField(),
                   'okres_obowiazywania': DateField(),
                   'comments': Textarea(attrs={'rows': 5}),
                   }
