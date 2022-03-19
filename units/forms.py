from django.forms import ModelForm
from units.models import Unit


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['powiat', 'unit_kind', 'address', 'kod_pocztowy', 'miasto', 'informacje', 'owner', 'aktywna']
        labels = {"powiat": "Powiat",
                  "unit_kind": "Rodzaj jednostki",
                  "address": "Adres",
                  "kod_pocztowy": "kod pocztowy",
                  "miasto": "Miasto",
                  "informacje": "Informacje",
                  "owner": 'Właściciel',
                  "aktywna": "Aktywna"}
