from django.forms import ModelForm
from units.models import Unit


class UnitForm(ModelForm):

    class Meta:
        model = Unit
        fields = ['county', 'type', 'address', 'zip_code', 'city', 'information', 'status']
        labels = {'county': 'Powiat',
                  'type': 'Rodzaj jednostki',
                  'address': 'Adres',
                  'zip_code': 'kod pocztowy',
                  'city': 'Miasto',
                  'information': 'Informacje',
                  'status': 'Status'}
