from django.forms import ModelForm
from main.models import Team, Telephone, OrganisationTelephone, AccessModule


class TeamForm(ModelForm):
    class Meta:
        model = Team
        field = ['team']
        labels = {'team': "Komrówka Wydziału"}


class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone
        field = ['team', 'position', 'fname', 'lname', 'no_tel_room', 'no_tel_private']
        labels = {'team': 'Zespół', 'position': 'Stanowisko', 'fname': 'Imię', 'lname': 'Nazwisko',
                  'no_tel_room': 'Nr. telefonu', 'no_tel_private': 'Nr komórkowy'}


class OrganisationTelephoneForm(ModelForm):
    class Meta:
        model = OrganisationTelephone
        fields = ['add_date', 'telephone_book']
        labels = {'telephone_book': 'Książka telefoniczna', 'add_date': 'Data dodania'}


class AccessModuleForm(ModelForm):
    class Meta:
        model = AccessModule
        fields = '__all__'
        labels = {'contractors_module': 'Moduł kontrahenci', 'contracts_module': 'Moduł umowy',
                  'investments_module': 'Moduł inwestycje', 'invoices_module': 'Moduł faktury'}
