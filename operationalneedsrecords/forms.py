from django.forms import ModelForm, DateInput, Textarea
from .models import NeedsLetter


class DateField(DateInput):
    input_type = "date"


class NeedsLetterForm(ModelForm):
    class Meta:
        model = NeedsLetter
        fields = "__all__"
        labels = {"receipt_date": "Data wpływu pisma", "case_sign": "Znak pisma", "unit": "Jednostka",
                  "case_description": "Opis sprawy", "case_type": "Rodzaj sprawy",
                  "registration_type": "Rodzaj zgłoszenia", "receipt_date_to_team": "Data wpływu do zespołu",
                  "case_sign_team": "Znak sprawy ZE", "information": "informacje", "execution_date": "Data realizacji",
                  "isDone": "Zrealizowane","employer":"Branżysta","author": "Autor"}
        exclude = ["author", "creation_date", "change"]
        widgets = {"receipt_date": DateField(),
                   "receipt_date_to_team": DateField(),
                   "execution_date": DateField(),
                   "case_description": Textarea(attrs={'rows': 4}),
                   "information": Textarea(attrs={"rows": 4})
                   }
