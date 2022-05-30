from django.forms import ModelForm, DateInput, Textarea
from invoices.models import InvoiceSell, InvoiceBuy


class DateField(DateInput):
    input_type = "date"


class InvoiceSellForm(ModelForm):
    class Meta:
        model = InvoiceSell
        fields = "__all__"
        label = {}
        exclude = ['creation_date', 'change_date', 'author']

        widgets = {
            'date': DateField(),
            'period_from': DateField(),
            'period_to': DateField(),
            'information': Textarea(attrs={'rows': 4})
        }


class InvoiceBuyForm(ModelForm):
    class Meta:
        model = InvoiceBuy
        fields = "__all__"
        label = {'date_receipt': 'Data wpływu', 'date_issue': 'Data wystawienia', 'Nr. faktury': 'no_invoice',
                 'Kwota': 'sum', 'date_of_payment': 'Data płatności', 'Kontrahent': 'contractor',
                 'period_from': 'Okres od',
                 'Okres do': 'period_to', 'information': 'Informacje'}
        exclude = ['creation_date', 'change_date', 'author']
        widgets = {
            'date_receipt': DateField(),
            'date_issue': DateField(),
            'period_from': DateField(),
            'period_to': DateField(),
            'date_of_payment': DateField(),
            'information': Textarea(attrs={'rows': 3})
        }
