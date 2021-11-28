from django import forms
from .models import Contractor


class ContractorForm(forms.Form):
    class Meta:
        model = Contractor
        fields = ["nazwa", "adres", "kod_pocztowy", "miasto", "informacje", "utworzenie", "autor"]
        labels = {'nazwa': 'Kontrahent',
                  'adres': 'Adres',
                  'kod_pocztowy': 'Kod pocztowy',
                  'miasto': 'Miasto',
                  'informacje': 'Informacje',
                  'utworzenie': 'utworzenie',
                  'autor': 'autor'
                  }
