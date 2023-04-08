from django.forms import ModelForm, DateInput, Textarea, widgets
from main.models import Team, OrganisationTelephone, AccessModule, Command, Employer, SecretariatTelephone, Car, \
    NecesseryFile


class DateField(DateInput):
    input_type = "date"


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('team', 'priority', 'active')
        labels = {'team': 'Komórka Wydziału', 'priority': 'Kolejność', 'active': 'Aktywny'}


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = (
            'id_swop', 'team', 'position', 'name', 'last_name', 'invoices_issues', 'industry_specialist', 'no_room',
            'industry', 'no_tel_room', 'no_tel_private', 'information', 'creation_date', 'change', 'author', 'deleted')
        labels = {'id_swop': 'id kadrowy', 'team': 'Zespół', 'position': 'Stanowisko', 'name': 'Imię',
                  'last_name': 'Nazwisko', 'invoices_issues': 'Wystawianie faktur',
                  'industry_specialist': 'Branżysta merytoryczny', 'industry': 'Branża', 'no_room': 'Nr.pokoju',
                  'no_tel_room': 'Nr. telefonu', 'no_tel_private': 'Nr komórkowy', 'information': 'Informacje',
                  'deleted': 'Usuń'}
        exclude = ['creation_date', 'change', 'author']
        widgets = {'information': Textarea(attrs={'rows': 3})}


class OrganisationTelephoneForm(ModelForm):
    class Meta:
        model = OrganisationTelephone
        fields = ('add_date', 'telephone_book')
        labels = {'telephone_book': 'Książka telefoniczna'}
        exclude = ['add_date']


class AccessModuleForm(ModelForm):
    class Meta:
        model = AccessModule
        fields = '__all__'
        labels = {'contractors_module': 'Moduł kontrahenci', 'contracts_module': 'Moduł umowy',
                  'investments_module': 'Moduł inwestycje', 'invoices_module': 'Moduł faktury',
                  'listregister_float_team_module': 'Moduł Ewidencja - Mieszkaniówka',
                  'listregister_exploatation_team_module': 'Moduł Ewidencja - Eksploatacja'}


class CommandForm(ModelForm):
    class Meta:
        model = Command
        fields = ('title', 'content', 'scan', 'change', 'create_date')
        labels = {'title': 'Tytuł', 'content': 'Treść', 'scan': 'Skan'}
        exclude = ['change', 'create_date']
        widgets = {'content': Textarea(attrs={'rows': 3}),
                   'title': widgets.TextInput(attrs={'placeholder': 'np: Polecenie nr 1 z dnia 01.01.2001'})}


class SecretariatTelephoneForm(ModelForm):
    class Meta:
        model = SecretariatTelephone
        fields = ('code', 'fax_number', 'secretariat_number', 'information', 'create')
        labels = {'code': 'Nr. kierunkowy', 'fax_number': 'Nr. faxu', 'secretariat_number': 'Nr. do sekretariatu',
                  'information': 'Informacje', 'create': 'Data utworzenia'}
        exclude = ['create']
        widgets = {'fax_number': widgets.TextInput(attrs={'pattern': '^[0-9]{3}-[0-9]{2}$', 'placeholder': '00-000'}),
                   'Nr. faxu': widgets.TextInput(attrs={'pattern': '^[0-9]{3}-[0-9]{2}$', 'placeholder': '00-000'})
                   }


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('rent_date', 'borrower', 'target', 'create_date', 'change', 'author')
        labels = {'rent_date': 'Data', 'borrower': 'Delegat', 'target': 'Cel'}
        exclude = ['change', 'create_date', 'author']
        widgets = {'target': Textarea(attrs={'rows': 2}),
                   'rent_date': DateField()
                   }


class NecesseryFileForm(ModelForm):
    class Model:
        model = NecesseryFile
        fields = ('title', 'file', 'create_date')
        labels = {'title': 'Nazwa', 'file': 'Plik', 'create_date': 'Data dodania'}
        widgets = {'create_date': DateField()}
