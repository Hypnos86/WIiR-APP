from django.forms import ModelForm
from units.models import Unit


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ('county', 'type', 'address', 'zip_code', 'city', 'information', 'status', 'change')
        labels = {'county': 'Powiat',
                  'type': 'Rodzaj jednostki',
                  'address': 'Adres',
                  'zip_code': 'kod pocztowy',
                  'city': 'Miasto',
                  'information': 'Informacje',
                  'remarks': 'Uwagi',
                  'status': 'Status'}
        exclude = ('change',)
