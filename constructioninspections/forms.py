from django.forms import ModelForm, Widget, Textarea, DateField
from main.forms import DateField
from constructioninspections.models import AirConditionerInspection, FireInspection, ElectricalInspectionOneYear, \
    ChimneyInspection, HeatingBoilerInspection, BuildingInspectionFiveYear, BuildingInspectionOneYear, \
    ElectricalInspectionFiveYear


class BuildingInspectionOneYearForm(ModelForm):
    class Meta:
        model = BuildingInspectionOneYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class BuildingInspectionFiveYearForm(ModelForm):
    class Meta:
        model = BuildingInspectionFiveYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class ChimneyInspectionForm(ModelForm):
    class Meta:
        model = ChimneyInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class ElectricalInspectionOneYearForm(ModelForm):
    class Meta:
        model = ElectricalInspectionOneYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class ElectricalInspectionFiveYearForm(ModelForm):
    class Meta:
        model = ElectricalInspectionFiveYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class HeatingBoilerInspectionForm(ModelForm):
    class Meta:
        model = HeatingBoilerInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class FireInspectionForm(ModelForm):
    class Meta:
        model = FireInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}


class AirConditionerInspectionForm(ModelForm):
    class Meta:
        model = AirConditionerInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu"}
        widgets = {"date_protocol": DateField(), "date_next_inspection": DateField()}
