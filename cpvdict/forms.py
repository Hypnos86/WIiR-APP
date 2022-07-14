from django.forms import ModelForm, DateInput
from main.forms import DateField
from cpvdict.models import Typecpv, OrderLimit, Order, Tax


class TypecpvForm(ModelForm):
    class Meta:
        model = Typecpv
        fields = ['no_cpv', 'name']
        labels = {'no_cpv': 'Kod CPV', 'name': 'Nazwa przedmiotu zamówienia wg CPV'}


class OrderLimitForm(ModelForm):
    class Meta:
        model = OrderLimit
        fields = ['year', 'euro_exchange_rate', 'limit_euro', 'limit_netto']
        labels = {'year': 'Rok', 'euro_exchange_rate': 'Kurs euro', 'limit_netto': 'Limit zamówień netto'}


class TaxForm(ModelForm):
    class Meta:
        model = Tax

        fields = ('vat',)
        labels = {'vat': 'Podatek'}


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'no_order', 'sum_netto','vat', 'sum_brutto', 'typeorder', 'genre', 'unit', 'contractor',
                  'brakedown', 'worker', 'content']
        exclude = ['author', 'create_date']
        labels = {'date': 'Data', 'no_order': 'Nr zamówienia', 'sum_netto': 'Kwota netto', 'vat':'vat',
                  'sum_brutto': 'kwota brutto', 'typeorder': 'Rodzaj zamoówienia', 'genre': 'ID Rodzajowości',
                  'unit': 'Jednostka', 'contractor': 'Wykonawca', 'brakedown': 'Awaria', 'content': 'Zakres'}

        widgets = {'date': DateField()}
