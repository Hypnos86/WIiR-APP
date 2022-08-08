from django.forms import ModelForm, DateInput, Textarea, widgets
from main.forms import DateField
from contracts.models import ContractImmovables, AnnexImmovables, ContractAuction, AnnexContractAuction, ContractMedia, \
    AnnexContractMedia


class ContractImmovablesForm(ModelForm):
    class Meta:
        model = ContractImmovables
        fields = ['id', 'date', 'no_contract', 'contractor', 'period_of_validity', 'usable_area', 'legal_basic',
                  'type_of_contract', 'rent_cost', 'electric_cost', 'gas_cost', 'water_cost', 'central_heating_cost',
                  'garbage_cost', 'garbage_tax_cost', 'property_cost', 'unit', 'scan', 'state', 'information',
                  'creation_date', 'change', 'author']

        field_order = ['id', 'date', 'no_contract', 'contractor', 'period_of_validity', 'usable_area', 'legal_basic',
                       'type_of_contract', 'rent_cost', 'electric_cost', 'gas_cost', 'water_cost',
                       'central_heating_cost', 'garbage_cost', 'garbage_tax_cost', 'property_cost', 'unit', 'scan',
                       'state', 'information', 'creation_date', 'change', 'author']

        labels = {'id': 'id', 'date': 'Data umowy', 'no_contract': 'Nr umowy', 'contractor': 'Kontrahent',
                  'legal_basic': 'Podstawa prawna', 'period_of_validity': 'Okres obowiązywania',
                  'type_of_contract': 'Rodzaj umowy', 'usable_area': 'Powiezchnia użytkowa', 'rent_cost': 'Czynsz',
                  'electric_cost': 'Prąd', 'gas_cost': 'Gaz', 'water_cost': 'Woda', 'central_heating_cost': 'C.O.',
                  'garbage_cost': 'Śmieci', 'garbage_tax_cost': 'Zagospodarowanie odpadami komunalnymi',
                  'property_cost': 'Podatek od nieruchomości', 'unit': 'Jednostka', 'scan': 'Skan umowy',
                  'state': 'Aktualna', 'information': 'Informacje'}

        exclude = ['creation_date', 'change', 'author']

        widgets = {'date': DateField(),
                   'period_of_validity': DateField(),
                   'information': Textarea(attrs={'rows': 5}),
                   }


class AnnexImmovablesForm(ModelForm):
    class Meta:
        model = AnnexImmovables

        fields = ['date_annex', 'scan_annex', 'creation_date', 'author']
        labels = {'date_annex': 'Data aneksu', 'scan_annex': 'Skan aneksu'}
        exclude = ['creation_date', 'author']
        widgets = {'date_annex': DateField()}


class ContractAuctionForm(ModelForm):
    class Meta:
        model = ContractAuction

        fields = ['id', 'date', 'no_contract', 'contractor', 'price', 'work_scope', 'legal_basic', 'end_date', 'unit',
                  'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percent',
                  'security_sum', 'worker', 'information', 'report', 'scan']
        labels = {'date': 'Data', 'no_contract': 'Nr. umowy', 'contractor': 'Wykonawca', 'price': 'Kwota umowy',
                  'work_scope': 'Zakres', 'legal_basic': 'Tryb zamówienia', 'end_date': 'Data zakończenia umowy',
                  'unit': 'Jednostka',
                  'last_report_date': 'Data ostatniego protokołu', 'guarantee': 'Rodzaj gwarancji',
                  'guarantee_period': 'Okres gwarancji', 'warranty_period': 'Okres rękojmi',
                  'security_percent': 'Procent zabezpieczenia',
                  'security_sum': 'Kwota zabezpieczenia', 'worker': 'Branżysta', 'information': 'Informacje',
                  'report': 'Raportowanie do ZZP',
                  'scan': 'Skan umowy'}
        exclude = ['creation_date', 'change', 'author']
        widgets = {'date': DateField(),
                   'end_date': DateField(),
                   'last_report_date': DateField(), }


class AnnexContractAuctionForm(ModelForm):
    class Meta:
        model = AnnexContractAuction
        fields = ['date', 'price_change', 'price_after_change', 'scope_changes', 'scan', 'creation_date', 'author']
        labels = {'date': 'Data aneksu', 'price_change': 'Zmiana wartości umowy', 'price_after_change': 'Kwota aneksu',
                  'scope_changes': 'Zakres zamian', 'scan': 'Skan aneksu'}
        exclude = ['creation_date', 'author']
        widgets = {'date': DateField()}


class ContractMediaForm(ModelForm):
    class Meta:
        model = ContractMedia
        fields = ['date', 'no_contract', 'contractor', 'type', 'legal_basic', 'content', 'period_of_validity', 'unit',
                  'information',
                  'scan', 'employer', 'state', 'creation_date', 'change_date', 'author']
        labels = {'date': 'Data umowy', 'no_contract': 'Nr.umowy', 'contractor': 'Wykonawca', 'type': 'Rodzaj umowy',
                  'legal_basic': 'Podstawa prawna',
                  'content': 'Treść', 'period_of_validity': 'Okres obowiązywania', 'unit': 'Jednostka',
                  'information': 'Informacje',
                  'scan': 'Skan', 'employer': 'Branżysta', 'state': 'Aktualna', 'creation_date': 'Data utworzenia',
                  'change_date': 'Zmiany', 'author': 'Autor'}
        exclude = ['creation_date', 'change_date', 'author']
        widgets = {'date': DateField(),
                   'period_of_validity': DateField(),
                   'information': Textarea(attrs={'rows': 3})}


class AnnexContractMediaForm(ModelForm):
    class Meta:
        model = AnnexContractMedia
        fields = ['date', 'scope_changes', 'scan', 'creation_date', 'author']
        labels = {'date': 'Data aneksu', 'scope_changes': 'Zakres zamian', 'scan': 'Skan aneksu'}
        exclude = ['creation_date', 'author']
        widgets = {'date': DateField()}
