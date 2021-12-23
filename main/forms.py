from django.forms import ModelForm
from main.models import Team, Telephone, OrganisationTelephone


class TeamForm(ModelForm):
    class Meta:
        model = Team
        field = ['team']
        labels = {'team': "Komrówka Wydziału"}


class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone
        field = ['team', 'position', 'fname', 'lname', 'numbtelbus', 'numbtelpri']
        labels = {'team': 'Zespół', 'position': 'Stanowisko', 'fname': 'Imię', 'lname': 'Nazwisko',
                  'numbtelbus': 'Nr. telefonu', 'numbtelpri': 'Nr komórkowy'}


class OrganisationTelephoneForm(ModelForm):
    class Meta:
        model = OrganisationTelephone
        fields = ['telephone_book']
        labels = {'telephone_book': 'Książka telefoniczna'}
