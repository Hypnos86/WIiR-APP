from django.forms import ModelForm
from invoices.models import Invoicesell


class InvoicesellForm(ModelForm):
    class Meta:
        model = Invoicesell
        fields = "__all__"
        exclude = ['create', 'change', 'uzytkownik']
