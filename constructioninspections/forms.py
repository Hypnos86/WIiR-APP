from django.forms import ModelForm, Widget, Textarea, DateField
from main.forms import DateField
from tinymce.widgets import TinyMCE
from constructioninspections.models import AirConditionerInspection, FireInspection, ElectricalInspectionOneYear, \
    ChimneyInspection, HeatingBoilerInspection, BuildingInspectionFiveYear, BuildingInspectionOneYear, \
    ElectricalInspectionFiveYear


class BuildingInspectionOneYearForm(ModelForm):
    class Meta:
        model = BuildingInspectionOneYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE(attrs={'cols': 5, 'rows': 3})}


class BuildingInspectionFiveYearForm(ModelForm):
    class Meta:
        model = BuildingInspectionFiveYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}


class ChimneyInspectionForm(ModelForm):
    class Meta:
        model = ChimneyInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}


class ElectricalInspectionOneYearForm(ModelForm):
    class Meta:
        model = ElectricalInspectionOneYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}


class ElectricalInspectionFiveYearForm(ModelForm):
    class Meta:
        model = ElectricalInspectionFiveYear
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}


class HeatingBoilerInspectionForm(ModelForm):
    class Meta:
        model = HeatingBoilerInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}


class FireInspectionForm(ModelForm):
    class Meta:
        model = FireInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}


class AirConditionerInspectionForm(ModelForm):
    class Meta:
        model = AirConditionerInspection
        fields = ("no_inventory", "inspection_name", "date_protocol", "conclusions", "date_next_inspection",
                  "technical_condition")
        exclude = ["creation_date", "change", "author"]
        labels = {"no_inventory": "Nr. inwentarzowy", "inspection_name": "Rodzaj przeglądu",
                  "date_protocol": "Data protokołu", "conclusions": "Wnioski",
                  "date_next_inspection": "Data następnego przeglądu", "technical_condition": "Stan techniczny"}
        widgets = {"date_protocol": DateField(),
                   "date_next_inspection": DateField(),
                   "cpmclusion": TinyMCE()}
