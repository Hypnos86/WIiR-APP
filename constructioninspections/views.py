from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspection, HeatingBoilerInspection, AirConditionerInspection, FireInspection


# Create your views here
@login_required
def contraction_inspection_menu(request):
    return render(request, "constructioninspections/base_inspections.html", {})


@login_required
def important_inspections(request):
    buildings_inspections_one_year = BuildingInspectionOneYear.objects.all().order_by("date_protocol")[:3]
    buildings_inspections_five_year = BuildingInspectionFiveYear.objects.all().order_by("date_protocol")[:3]
    chimneys_inspections = ChimneyInspection.objects.all().order_by("date_protocol")[:3]
    electricial_inspections = ElectricalInspection.objects.all().order_by("date_protocol")[:3]
    heating_boiler_inspections = HeatingBoilerInspection.objects.all().order_by("date_protocol")[:3]
    air_conditioners_inspection = AirConditionerInspection.objects.all().order_by("date_protocol")[:3]
    fire_inspections = FireInspection.objects.all().order_by("date_protocol")[:3]

    context = {"buildings_inspections_one_year": buildings_inspections_one_year,
               "buildings_inspections_five_year": buildings_inspections_five_year,
               "chimneys_inspections": chimneys_inspections, "electricial_inspections": electricial_inspections,
               "air_conditioners_inspection": air_conditioners_inspection,
               "heating_boiler_inspections": heating_boiler_inspections,
               "fire_inspections": fire_inspections}
    return render(request, "constructioninspections/inspections.html", context)


@login_required
def create_buildings_inspections_choise(request):
    return render(request, "constructioninspections/buildings_inspection_all_list.html", {})


@login_required
def create_buildings_one_year_inspections(request):
    return render(request, "constructioninspections/buildings_one_year_inspection.html")


@login_required
def create_buildings_five_year_inspections(request):
    return render(request, "constructioninspections/buildings_five_year_inspection.html")


@login_required
def create_chimney_inspection_list(request):
    objects = ChimneyInspection.objects.all()
    return render(request, "constructioninspections/chimneys_inspection_list.html", {"objects": objects})


@login_required
def create_electrical_inspection_list(request):
    objects = ElectricalInspection.objects.all()
    return render(request, "constructioninspections/electrical_inspection_list.html", {"objects": objects})


@login_required
def create_heating_boilers_inspection_list(request):
    objects = HeatingBoilerInspection.objects.all()
    return render(request, "constructioninspections/heating_boilers_inspection_list.html", {"objects": objects})


@login_required
def create_air_conditioners_inspection_list(request):
    objects = AirConditionerInspection.objects.all()
    return render(request, "constructioninspections/air_conditioners_inspection_list.html", {"objects": objects})


@login_required
def create_fire_inspection_list(request):
    objects = FireInspection.objects.all()
    return render(request, "constructioninspections/fire_inspection_list.html", {"objects": objects})
