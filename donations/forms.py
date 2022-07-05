from django.forms import ModelForm, DateInput, Textarea
from donations.models import Application
from main.forms import DateField


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['character', 'date_receipt', 'date_return', 'no_application', 'no_agreement', 'date_agreement',
                  'donation_type', 'financial_type', 'presenter', 'sum', 'settlement_date', 'unit', 'subject',
                  'information', 'creation_date', 'change', 'author']
        label = {'character': 'Znak', 'date_receipt': 'Data wpływu', 'date_return': 'Data zwrotu',
                 'no_application': 'Nr. wniosku', 'no_agreement': 'Nr. porozumienia',
                 'date_agreement': 'Data porozumienia',
                 'donation_type': 'Rodzaj darowizny', 'financial_type': 'Rodzaj środków', 'presenter': 'Darczyńca',
                 'sum': 'Kwota', 'settlement_date': 'Data rozliczenia', 'unit': 'Jednostka',
                 'subject': 'Przedmiot porozumienia', 'information': 'Informacje', }
        exclude = ['creation_date', 'change', 'author']
        widgets = {'date_receipt': DateField(),
                   'date_return': DateField(),
                   'date_agreement': DateField(),
                   'settlement_date': DateField(),
                   'information': Textarea(attrs={'rows': 3}),
                   }