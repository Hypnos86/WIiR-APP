from django.forms import ModelForm
from contractors.models import Contractorsell, Contractorbuy


class ContractorsellForm(ModelForm):
    class Meta:
        model = Contractorsell
        fields = ["nazwa", "nip", "adres", "kod_pocztowy", "miasto", "informacje", "utworzenie", "autor"]
        exclude = ["utworzenie", "autor"]
        labels = {'nazwa': 'Kontrahent',
                  "nip": 'NIP',
                  'adres': 'Adres',
                  'kod_pocztowy': 'Kod pocztowy',
                  'miasto': 'Miasto',
                  'informacje': 'Informacje',
                  'utworzenie': 'Utworzenie',
                  'autor': 'Autor'
                  }


class ContractorbuyForm(ModelForm):
    class Meta:
        model = Contractorbuy
        fields = ["nazwa", "nip", "adres", "kod_pocztowy", "miasto", "informacje", "utworzenie", "autor"]
        exclude = ["utworzenie", "autor"]
        labels = {'nazwa': 'Kontrahent',
                  'nip': 'NIP',
                  'adres': 'Adres',
                  'kod_pocztowy': 'Kod pocztowy',
                  'miasto': 'Miasto',
                  'informacje': 'Informacje',
                  'utworzenie': 'Utworzenie',
                  'autor': 'Autor'
                  }
