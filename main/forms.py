from django.forms import ModelForm, DateInput, Textarea
from main.models import Team, OrganisationTelephone, AccessModule, Command, Employer


class DateField(DateInput):
    input_type = "date"


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team', 'active']
        label = {'team': 'Komrówka Wydziału', 'active': 'Aktywny'}


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = ['team', 'position', 'name', 'last_name', 'industry_specialist', 'no_room', 'industry', 'no_tel_room',
                  'no_tel_private', 'information', 'creation_date', 'change', 'author', 'deleted']
        label = {'team': 'Zespół', 'position': 'Stanowisko', 'name': 'Imię', 'last_name': 'Nazwisko',
                 'industry_specialist': 'Branżysta', 'industry': 'Branża', 'no_room': 'Nr.pokoju',
                 'no_tel_room': 'Nr. telefonu', 'no_tel_private': 'Nr komórkowy', 'information': 'Informacje',
                 'deleted': 'Usuń'}
        exclude = ['creation_date', 'change', 'author']

        widgets = {'information': Textarea(attrs={'rows': 3}),
                   }


class OrganisationTelephoneForm(ModelForm):
    class Meta:
        model = OrganisationTelephone
        fields = ['add_date', 'telephone_book']
        label = {'telephone_book': 'Książka telefoniczna'}
        exclude = ['add_date']


class AccessModuleForm(ModelForm):
    class Meta:
        model = AccessModule
        fields = '__all__'
        label = {'contractors_module': 'Moduł kontrahenci', 'contracts_module': 'Moduł umowy',
                 'investments_module': 'Moduł inwestycje', 'invoices_module': 'Moduł faktury',
                 'listregister_float_team_module': 'Moduł Ewidencja - Mieszkaniówka',
                 'listregister_exploatation_team_module': 'Moduł Ewidencja - Eksploatacja'}


class CommandsForm(ModelForm):
    class Meta:
        model = Command
        fields = ['title', 'content', 'scan', 'create_date']
        label = {'title': 'Tytuł', 'content': 'Treść'}
        exclude = ['create_date']
