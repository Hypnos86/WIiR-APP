from django.forms import ModelForm, DateInput, Textarea
from invoices.models import Invoicesell


class DateField(DateInput):
    input_type = "date"


class InvoicesellForm(ModelForm):
    class Meta:
        model = Invoicesell
        fields = "__all__"
        exclude = ['create', 'change', 'author']

        widgets = {
            'data': DateField(),
            'period_from': DateField(),
            'period_to': DateField(),
            'comments': Textarea(attrs={'rows': 3})
        }