from django.forms import ModelForm, DateInput, Textarea
from contracts.models import ContractImmovables, AneksImmovables, ContractAuction, AneksContractAuction


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


class ContractAuctionForm(ModelForm):
    class Meta:
        model = ContractAuction

        fields = ['date', 'no_contract', 'contractor', 'price', 'work_scope', 'legal_basic_zzp', 'end_date', 'unit',
                  'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percent',
                  'contract_security', 'inspector', 'information', 'scan', 'create', 'change', 'author']
        labels = {'date': 'Data', 'no_contract': 'Nr. umowy', 'contractor': 'Wykonawca', 'price': 'Kwota umowy',
                  'work_scope': 'Zakres', 'legal_basic_zzp': 'Tryb zamówienia', 'end_date': 'Data zakończenia umowy',
                  'unit': 'Jednostka',
                  'last_report_date': 'Data ostatniego protokołu', 'guarantee': 'Rodzaj gwarancji',
                  'guarantee_period': 'Okres gwarancji', 'warranty_period': 'Okres rękojmi',
                  'security_percent': 'Procent zabezpieczenia',
                  'contract_security': 'Kwota zabezpieczenia', 'inspector': 'Inspektor', 'information': 'Informacje',
                  'scan': 'Skan umowy'}
        exclude = ['create', 'change', 'author']
        widgets = {'date': DateField(),
                   'end_date': DateField(),
                   'last_report_date': DateField(), }
