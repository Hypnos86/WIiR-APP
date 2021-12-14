from django.forms import ModelForm, Textarea
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
        widgets = {'informacje': Textarea(attrs={'rows': 5})
                   }