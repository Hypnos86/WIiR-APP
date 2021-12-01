from django.forms import ModelForm
from units.models import Jednostka


class JednotkskaForm(ModelForm):
    class Meta:
        model = Jednostka
        fields = ['powiat', 'rodzaj', 'adres', 'kod_pocztowy', 'miasto', 'informacje', 'aktywna']
        labels = {"powiat": "Powiat",
                  "rodzaj": "Rodzaj jednostki",
                  "adres": "Adres",
                  "kod_pocztowy": "kod pocztowy",
                  "miasto": "Miasto",
                  "informacje": "Informacje",
                  "aktywna": "Aktywna"}
