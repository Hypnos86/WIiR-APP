from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspection, HeatingBoilerInspection, AirConditionerInspection, FireInspection, TypeInspection
from constructioninspections.forms import AirConditionerInspectionForm


# Create your views here

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
    return render(request, "construction_inspections/priority_inspections.html", context)


@login_required
def buildings_inspections_choise(request):
    return render(request, "construction_inspections/buildings_choise_popup.html", {})


@login_required
def create_buildings_one_year_inspections(request):
    return render(request, "construction_inspections/buildings_one_year_inspection.html")


@login_required
def create_buildings_five_year_inspections(request):
    return render(request, "construction_inspections/buildings_five_year_inspection.html")


@login_required
def create_chimney_inspection_list(request):
    objects = ChimneyInspection.objects.all()
    return render(request, "construction_inspections/chimneys_inspection_list.html", {"objects": objects})


@login_required
def create_electrical_inspection_list(request):
    objects = ElectricalInspection.objects.all()
    return render(request, "construction_inspections/electrical_inspection_list.html", {"objects": objects})


@login_required
def create_heating_boilers_inspection_list(request):
    objects = HeatingBoilerInspection.objects.all()
    return render(request, "construction_inspections/heating_boilers_inspection_list.html", {"objects": objects})


@login_required
def create_air_conditioners_inspection_list(request):
    objects = AirConditionerInspection.objects.all()
    return render(request, "construction_inspections/air_conditioners_inspection_list.html", {"objects": objects})


@login_required
def create_fire_inspection_list(request):
    objects = FireInspection.objects.all()
    return render(request, "construction_inspections/fire_inspection_list.html", {"objects": objects})


# @login_required
# def add_new_protocol(request, typeInspectinos):
#     buildings_one_year = get_object_or_404(create_buildings_one_year_inspections)
#     buildings_one_year.fields['inspection_name'].queryset = TypeInspection.objects.all().filter(inspection_name="aa")
#
#     form = InspectionForms(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             pass
