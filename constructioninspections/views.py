from django.shortcuts import render
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection


# Create your views here.
def contraction_inspection_menu(request):
    objects = BuildingInspectionOneYear.objects.all().order_by("date_protocol"), BuildingInspectionFiveYear.objects.all().order_by("date_protocol"), ChimneyInspection.objects.all().order_by("date_protocol")
    return render(request, "constructioninspections/navigation.html", {"objects": objects})
