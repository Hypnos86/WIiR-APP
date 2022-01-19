from django.forms import ModelForm, Textarea, widgets
from contractors.models import Contractor


class ContractorsellForm(ModelForm):
    class Meta:
        model = Contractor
        fields = ["nocuntractor", "nazwa", "nip", "adres", "kod_pocztowy", "miasto", "informacje", "utworzenie",
                  "autor"]
        exclude = ["utworzenie", "autor"]
        labels = {'nocuntractor': 'Nr. kontrahenta', 'nazwa': 'Kontrahent',
                  "nip": 'NIP',
                  'adres': 'Adres',
                  'kod_pocztowy': 'Kod pocztowy',
                  'miasto': 'Miasto',
                  'informacje': 'Informacje',
                  'utworzenie': 'Utworzenie',
                  'autor': 'Autor'
                  }
        widgets = {'nocuntractor': widgets.TextInput(attrs={'placeholder': 'wpisz nr kontrahenta zgodny z nr SWOP'}),
                   'informacje': Textarea(attrs={'rows': 5}),
                   'nip': widgets.TextInput(
                       attrs={'pattern': '^[0-9]{3}-[0-9]{2}-[0-9]{2}-[0-9]{3}$', 'placeholder': 'xxx-xx-xx-xxx'}),
                   'kod_pocztowy': widgets.TextInput(attrs={'pattern': '^[0-9]{2}-[0-9]{3}$', 'placeholder': 'xx-xxx'})
                   }
