from django.forms import ModelForm, DateInput, Textarea
from contracts.models import ContractImmovables, AneksImmovables


class DateField(DateInput):
    input_type = "date"


class ContractimmovablesForm(ModelForm):
    class Meta:
        model = ContractImmovables
        fields = ['data_umowy', 'nrumowy', 'kontrahent', 'okres_obowiazywania', 'pow_uzyczona', 'podstawa',
                  'rodzaj', 'koszt_czynsz', 'koszt_prad', 'koszt_gaz', 'koszt_woda', 'koszt_co', 'koszt_smieci',
                  'koszt_podsmiec', 'koszt_podnier', 'unit', 'skan', 'stan', 'comments', 'archives', 'create',
                  'change', 'author']

        field_order = ['data_umowy', 'nrumowy', 'kontrahent', 'okres_obowiazywania', 'pow_uzyczona', 'podstawa',
                       'rodzaj', 'koszt_czynsz', 'koszt_prad', 'koszt_gaz', 'koszt_woda', 'koszt_co', 'koszt_smieci',
                       'koszt_podsmiec', 'koszt_podnier', 'unit', 'skan', 'stan', 'comments', 'archives', 'create',
                       'change', 'author']

        labels = {'data_umowy': 'Data umowy', 'nrumowy': 'Nr umowy', 'kontrahent': 'Kontrahent',
                  'podstawa': 'Podstawa prawda', 'okres_obowiazywania': 'Okres obowiązywania', 'rodzaj': 'Rodzaj umowy',
                  'pow_uzyczona': 'Powiezchnia użytkowa', 'koszt_czynsz': 'Czynsz',
                  'koszt_prad': 'Prąd', 'koszt_gaz': 'Gaz', 'koszt_woda': 'Woda', 'koszt_co': 'C.O.',
                  'koszt_smieci': 'Śmieci',
                  'koszt_podsmiec': 'Zagospodarowanie odpadami komunalnymi',
                  'koszt_podnier': 'Podatek od nieruchomości',
                  'unit': 'Jednostka', 'skan': 'Skan umowy', 'stan': 'Stan umowy', 'comments': 'Informacje'}

        exclude = ['archives', 'create', 'change', 'author']

        widgets = {'data_umowy': DateField(),
                   'okres_obowiazywania': DateField(),
                   'comments': Textarea(attrs={'rows': 3}),
                   }


class AneksForm(ModelForm):
    class Meta:
        model = AneksImmovables

        fields = ['data_aneksu', 'skan_aneksu', 'create', 'autor']
        labels = {'data_aneksu': 'Data aneksu', 'skan_aneksu': 'Skan aneksu'}
        exclude = ['create', 'autor']
        widgets = {'data_aneksu': DateField()}
