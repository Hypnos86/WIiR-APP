from django.forms import ModelForm, DateInput, Textarea, widgets, DecimalField
from contracts.models import ContractImmovables, AnnexImmovables, ContractAuction
from main.models import Employer


class DateField(DateInput):
    input_type = "date"


class ContractImmovablesForm(ModelForm):
    class Meta:
        model = ContractImmovables
        fields = ['date', 'no_contract', 'contractor', 'period_of_validity', 'usable_area', 'legal_basic',
                  'type_of_contract', 'rent_cost', 'electric_cost', 'gas_cost', 'water_cost', 'central_heating_cost',
                  'garbage_cost', 'garbage_tax_cost', 'property_cost', 'unit', 'scan', 'state', 'information',
                  'creation_date', 'change', 'author']

        field_order = ['date', 'no_contract', 'contractor', 'period_of_validity', 'usable_area', 'legal_basic',
                       'type_of_contract', 'rent_cost', 'electric_cost', 'gas_cost', 'water_cost',
                       'central_heating_cost', 'garbage_cost', 'garbage_tax_cost', 'property_cost', 'unit', 'scan',
                       'state', 'information', 'creation_date', 'change', 'author']

        labels = {'date': 'Data umowy', 'no_contract': 'Nr umowy', 'contractor': 'Kontrahent',
                  'legal_basic': 'Podstawa prawda', 'period_of_validity': 'Okres obowiązywania',
                  'type_of_contract': 'Rodzaj umowy', 'usable_area': 'Powiezchnia użytkowa', 'rent_cost': 'Czynsz',
                  'electric_cost': 'Prąd', 'gas_cost': 'Gaz', 'water_cost': 'Woda', 'central_heating_cost': 'C.O.',
                  'garbage_cost': 'Śmieci', 'garbage_tax_cost': 'Zagospodarowanie odpadami komunalnymi',
                  'property_cost': 'Podatek od nieruchomości', 'unit': 'Jednostka', 'scan': 'Skan umowy',
                  'state': 'Stan umowy', 'information': 'Informacje'}

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

        fields = ['date', 'no_contract', 'contractor', 'price', 'work_scope', 'legal_basic', 'end_date', 'unit',
                  'last_report_date', 'guarantee', 'guarantee_period', 'warranty_period', 'security_percent',
                  'security_sum', 'worker', 'information', 'report', 'scan', 'creation_date', 'change_date',
                  'author']
        labels = {'date': 'Data', 'no_contract': 'Nr. umowy', 'contractor': 'Wykonawca', 'price': 'Kwota umowy',
                  'work_scope': 'Zakres', 'legal_basic': 'Tryb zamówienia', 'end_date': 'Data zakończenia umowy',
                  'unit': 'Jednostka',
                  'last_report_date': 'Data ostatniego protokołu', 'guarantee': 'Rodzaj gwarancji',
                  'guarantee_period': 'Okres gwarancji', 'warranty_period': 'Okres rękojmi',
                  'security_percent': 'Procent zabezpieczenia',
                  'security_sum': 'Kwota zabezpieczenia', 'worker': 'Pracownik', 'information': 'Informacje',
                  'report': 'Raportowanie do ZZP',
                  'scan': 'Skan umowy'}
        exclude = ['creation_date', 'change_date', 'author']
        widgets = {'date': DateField(),
                   'end_date': DateField(),
                   'last_report_date': DateField(), }

        def __init__(self, worker, *args, **kwargs):
            super(ContractAuctionForm, self).__init__(*args, **kwargs)
            self.fields['worker'].queryset = Employer.objects.filter(industry_specialist=True)
