from django.forms import ModelForm, DateInput
from main.forms import DateField
from cpvdict.models import Typecpv, OrderLimit, Order



class TypecpvForm(ModelForm):
    class Meta:
        model = Typecpv
        fields = ['no_cpv', 'name']
        labels = {'no_cpv': 'Kod CPV', 'name': 'Nazwa przedmiotu zamówienia wg CPV'}


class OrderLimitForm(ModelForm):
    class Meta:
        model = OrderLimit
        fields = ['limit']
        labels = {'limit': 'Limit zamówień'}


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'no_order', 'sum', 'typeorder', 'genre', 'unit', 'contractor', 'brakedown', 'worker', 'content']
        exclude = ['author', 'create_date']
        labels = {'date': 'Data', 'no_order': 'Nr zamówienia', 'sum': 'Szacowana kwota',
                  'typeorder': 'Rodzaj zamoówienia', 'genre': 'ID Rodzajowości', 'unit': 'Jednostka',
                  'contractor': 'Wykonawca', 'brakedown': 'Awaria', 'content': 'Zakres'}

        widgets = {'date': DateField()}
