from django.forms import ModelForm, DateInput, Textarea, widgets
from main.models import Team, OrganisationTelephone, AccessModule, Command, Employer, SecretariatTelephone, Car


class DateField(DateInput):
    input_type = "date"


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('team', 'priority', 'active')
        labels = {'team': 'Komrówka Wydziału', 'priority': 'Kolejność', 'active': 'Aktywny'}


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


class CommandsForm(ModelForm):
    class Meta:
        model = Command
        fields = ('title', 'content', 'scan', 'change', 'create_date')
        labels = {'title': 'Tytuł', 'content': 'Treść'}
        exclude = ['change', 'create_date']
        widgets = {'content': Textarea(attrs={'rows': 3})}


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
        fields = ('date', 'borrower', 'target', 'create_date', 'change', 'author')
        labels = {'date': 'Data', 'borrower': 'Delegat', 'target': 'Cel'}
        exclude = ['change', 'create_date']
        widgets = {'target': Textarea(attrs={'rows': 2}),
                   'date': DateField()
                   }
