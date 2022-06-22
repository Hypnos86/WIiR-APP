from django.forms import ModelForm, Textarea, widgets
from contractors.models import Contractor


class ContractorsellForm(ModelForm):
    class Meta:
        model = Contractor
        fields = ['no_contractor', 'name', 'nip', 'address', 'zip_code', 'city', 'information', 'creation_date',
                  'author']
        exclude = ['creation_date', 'author']
        labels = {'no_contractor': 'Nr. kontrahenta',
                  'name': 'Kontrahent',
                  "nip": 'NIP',
                  'address': 'Adres',
                  'zuo_code': 'Kod pocztowy',
                  'city': 'Miasto',
                  'information': 'Informacje',
                  'creation_date': 'Utworzenie',
                  'author': 'Autor'
                  }
        widgets = {'no_contractor': widgets.TextInput(attrs={'placeholder': 'nr kontrahenta zgodny z nr SWOP'}),
                   'name': widgets.TextInput(attrs={'placeholder': 'Nazwa kontrahenta'}),
                   'address': widgets.TextInput(attrs={'placeholder': 'Ulica'}),
                   'information': Textarea(attrs={'rows': 5}),
                   'nip': widgets.TextInput(attrs={'pattern': '^[0-9]{10}$', 'placeholder': '0123456789'}),
                   'zip_code': widgets.TextInput(attrs={'pattern': '^[0-9]{2}-[0-9]{3}$', 'placeholder': '00-000'}),
                   'citye': widgets.TextInput(attrs={'placeholder': 'Miasto'})
                   }
