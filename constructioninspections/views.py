from django.shortcuts import render
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspection, HeatingBoilerInspection, AirConditionerInspection, FireInspection


# Create your views here.
def contraction_inspection_menu(request):
    objects = BuildingInspectionOneYear.objects.all().order_by("date_protocol"), \
              BuildingInspectionFiveYear.objects.all().order_by("date_protocol"), \
              ChimneyInspection.objects.all().order_by("date_protocol"), \
              ElectricalInspection.objects.all().order_by("date_protocol"), \
              AirConditionerInspection.objects.all().order_by("date_protocol"), \
              FireInspection.objects.all().order_by("date_protocol")
    return render(request, "constructioninspections/navigation.html", {"objects": objects})


def create_buildings_inspections_choise(request):
    return render(request, "constructioninspections/buildings_inspection_all_list.html", {})


def create_buildings_one_year_inspections(request):
    return render(request, "constructioninspections/buildings_one_year_inspection.html")


def create_buildings_five_year_inspections(request):
    return render(request, "constructioninspections/buildings_five_year_inspection.html")


def create_chimney_inspection_list(request):
    objects = ChimneyInspection.objects.all()
    return render(request, "constructioninspections/chimneys_inspection_list.html", {"objects": objects})


def create_electrical_inspection_list(request):
    objects = ElectricalInspection.objects.all()
    return render(request, "constructioninspections/electrical_inspection_list.html", {"objects": objects})


def create_heating_boilers_inspection_list(request):
    objects = HeatingBoilerInspection.objects.all()
    return render(request, "constructioninspections/heating_boilers_inspection_list.html", {"objects": objects})


def create_air_conditioners_inspection_list(request):
    objects = AirConditionerInspection.objects.all()
    return render(request, "constructioninspections/air_conditioners_inspection_list.html", {"objects": objects})


def create_fire_inspection_list(request):
    objects = FireInspection.objects.all()
    return render(request, "constructioninspections/fire_inspection_list.html", {"objects": objects})
