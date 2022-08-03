from django.forms import ModelForm
from django.forms.widgets import Textarea
from units.models import Unit


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = (
            'county', 'type', 'address', 'zip_code', 'city', 'information', 'manager', 'comments', 'status', 'change',
            'author')
        labels = {'county': 'Powiat',
                  'type': 'Rodzaj jednostki',
                  'address': 'Adres',
                  'zip_code': 'kod pocztowy',
                  'city': 'Miasto',
                  'information': 'Nazwa obiektu',
                  'manager': 'Zarządca',
                  'comments': 'Informacje',
                  'remarks': 'Uwagi',
                  'status': 'Aktualna'}
        exclude = ('change', 'author')
        widgets = {'information': Textarea(attrs={'rows': 1}),
                   'comments': Textarea(attrs={'rows': 3})}
