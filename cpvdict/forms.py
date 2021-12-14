from django.forms import ModelForm
from cpvdict.models import Typecpv


class TypecpvForm(ModelForm):
    class Meta:
        model = Typecpv
        fields = ['nocpv', 'name']
        labels = {'nocpv': 'Kod CPV', 'name': 'Nazwa przedmiotu zamówienia wg CPV'}
