from django.forms import ModelForm, DateInput, Textarea
from invoices.models import InvoiceSell, InvoiceBuy


class DateField(DateInput):
    input_type = "date"


class InvoiceSellForm(ModelForm):
    class Meta:
        model = InvoiceSell
        fields = "__all__"
        label = {'date': 'Data wystawienia', 'no_invoice': 'Nr. faktury', 'contractor': 'Kontrahent', 'sum': 'Kwota',
                 'county': 'Powiat', 'date_of_payment': 'Termin płatności', 'period_from': 'Okres od',
                 'period_to': 'Okres do', 'creator': 'Osoba wystawiająca', 'information': 'Informacje',
                 'creation_date': 'Data utworzenia', 'change_date': 'Zmiana', 'author': 'Autor'}
        exclude = ['creation_date', 'change_date', 'author']
        widgets = {
            'date': DateField(),
            'period_from': DateField(),
            'period_to': DateField(),
            'date_of_payment': DateField(),
            'information': Textarea(attrs={'rows': 4})
        }


class InvoiceBuyForm(ModelForm):
    class Meta:
        model = InvoiceBuy
        fields = "__all__"
        label = {'date_receipt': 'Data wpływu', 'date_issue': 'Data wystawienia', 'no_invoice': 'Nr. faktury',
                 'sum': 'Kwota', 'date_of_payment': 'Termin płatności', 'contractor': 'Kontrahent',
                 'period_from': 'Okres od', 'period_to': 'Okres do', 'information': 'Informacje'}
        exclude = ['creation_date', 'change_date', 'author']
        widgets = {
            'date_receipt': DateField(),
            'date_issue': DateField(),
            'period_from': DateField(),
            'period_to': DateField(),
            'date_of_payment': DateField(),
            'information': Textarea(attrs={'rows': 3})
        }
