from django.forms import ModelForm
from businessflats.models import OfficialFlat


class OfficialFlatForm(ModelForm):
    class Meta:
        model = OfficialFlat

        fields = ('address', 'area', 'room_numbers', 'flor', 'state', 'information')
        labels = {'address': 'Adres', 'area': 'Powierzchnia', 'room_numbers': 'Ilość pomieszczeń', 'flor': 'Piętro',
                 'state': 'Wolne', 'information': 'Informacje'}
        exclude = ['creation_date', 'change', 'author']
