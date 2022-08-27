from django.forms import ModelForm, Textarea
from fixedasset.models import Building


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ("unit", "no_inventory", "building_name", "kind", "usable_area", "volume", "information", "state",
                  "creation_date", "change", "author")
        labels = {"unit": "Jednostka", "no_inventory": "Nr. inwentarzowy", "building_name": "Nazwa budynku",
                  "kind": "Typ budynku", "usable_area": "Powierzchnia użytkowa", "volume": "Kubatura",
                  "information": "Informacje", "state": "Aktywny"}
        exclude = ["creation_date", "change", "author"]
        widgets = {
            "information": Textarea(attrs={"rows": 3})
        }
