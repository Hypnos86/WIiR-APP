from django.forms import ModelForm

from .models import Contractor


class ContractorForm(ModelForm):
    class Meta:
        model = Contractor
        fields = ["nazwa", "adres", "kod_pocztowy", "miasto", "informacje", "utworzenie", "autor"]
        exclude = ["utworzenie", "autor"]
        labels = {'nazwa': 'Kontrahent',
                  'adres': 'Adres',
                  'kod_pocztowy': 'Kod pocztowy',
                  'miasto': 'Miasto',
                  'informacje': 'Informacje',
                  'utworzenie': 'Utworzenie',
                  'autor': 'Autor'
                  }
