from django.forms import ModelForm
from cpvdict.models import Typecpv, Order


class TypecpvForm(ModelForm):
    class Meta:
        model = Typecpv
        fields = ['no_cpv', 'name']
        labels = {'no_cpv': 'Kod CPV', 'name': 'Nazwa przedmiotu zamówienia wg CPV'}


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'no_order', 'sum', 'type', 'cpv_id', 'unit', 'brakedown', 'content']
        exclude = ['author']
        labels = {'date': 'Data', 'no_order': 'Nr zamówienia', 'sum': 'Szacowana kwota', 'type': 'Rodzaj zamoówienia',
                  'cpv_id': 'ID Rodzajowości', 'unit': 'Jednostka', 'brakedown': 'Awaria', 'content': 'Zakres'}
