from django.forms import ModelForm, DateInput
from invoices.models import Invoicesell


class PeriodDate(DateInput):
    input_type = "date"


class InvoicesellForm(ModelForm):
    period_from = PeriodDate()

    class Meta:
        model = Invoicesell
        fields = "__all__"
        exclude = ['create', 'change', 'autor']

    # widgets = {
    #     'period_from': PeriodDate(format=('%m.%Y'),
    #                               attrs={'class': 'form-control', 'placeholder': 'Wybierz', 'type': 'date'}),
    #     'period_to': PeriodDate(format=('%m.%Y'),
    #                             attrs={'class': 'form-control', 'placeholder': 'Wybierz', 'type': 'date'})}
    # 'period_to': PeriodDate(format=('%m.%Y'), attrs={'class': 'form-control', 'placeholder': 'Wybierz okres od'})}
