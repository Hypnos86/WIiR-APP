from django.forms import ModelForm, Widget, Textarea, DateField
from main.forms import DateField
from constructioninspections.models import AirConditionerInspection, FireInspection, ElectricalInspection, \
    ChimneyInspection, HeatingBoilerInspection, BuildingInspectionFiveYear, BuildingInspectionOneYear


class AirConditionerInspectionForm(ModelForm):
    class Meta:
        model = AirConditionerInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


