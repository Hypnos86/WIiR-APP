from django.forms import ModelForm, widgets
from businessflats.models import OfficialFlat


class OfficialFlatForm(ModelForm):
    class Meta:
        model = OfficialFlat

        fields = ('address', 'zip_code', 'city', 'area', 'room_numbers', 'flor', 'state', 'information')
        labels = {'address': 'Adres', 'zip_code': 'Kod pocztowy', 'city': 'Miasto', 'area': 'Powierzchnia',
                  'room_numbers': 'Ilość pomieszczeń', 'flor': 'Piętro',
                  'state': 'Wolne', 'information': 'Informacje'}
        exclude = ['creation_date', 'change', 'author']
        widgets = {
            'zip_code': widgets.TextInput(attrs={'pattern': '^[0-9]{2}-[0-9]{3}$', 'placeholder': 'xx-xxx'})
        }