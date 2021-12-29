from django.forms import ModelForm
from cpvdict.models import Typecpv


class TypecpvForm(ModelForm):
    class Meta:
        model = Typecpv
        fields = ['no_cpv', 'name']
        labels = {'no_cpv': 'Kod CPV', 'name': 'Nazwa przedmiotu zamówienia wg CPV'}
