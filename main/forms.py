from django.forms import ModelForm
from main.models import Telephone


class TelephoneForm(ModelForm):
    class Meta:
        name = Telephone
        field = ['team', 'position', 'fname', 'lname', 'numbtelbus', 'numbtelpri']
        labels = {'team': 'Zespół', 'position': 'Stanowisko', 'fname': 'Imię', 'lname': 'Nazwisko',
                  'numbtelbus': 'Nr. telefonu', 'numbtelpri': 'Nr komórkowy'}
