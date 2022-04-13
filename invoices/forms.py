from django.forms import ModelForm, DateInput, Textarea
from invoices.models import InvoiceSell


class DateField(DateInput):
    input_type = "date"


class InvoiceSellForm(ModelForm):
    class Meta:
        model = InvoiceSell
        fields = "__all__"
        exclude = ['creation_date', 'change_date', 'author']

        widgets = {
            'date': DateField(),
            'period_from': DateField(),
            'period_to': DateField(),
            'information': Textarea(attrs={'rows': 3})
        }