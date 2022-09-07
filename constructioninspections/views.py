from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
from datetime import date
from django.shortcuts import render, get_object_or_404
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspection, HeatingBoilerInspection, AirConditionerInspection, FireInspection, TypeInspection
# from constructioninspections.forms import AirConditionerInspectionForm
from fixedasset.models import Building
from units.models import Unit


# Create your views here

@login_required
def important_inspections(request):
    next_date = date.today() + relativedelta(months=+3)
    print(f"Data za miesiac: {next_date}")

    buildings_inspections_one_year = []
    buildings_inspections_one_year.sort()
    buildings_inspections_five_year = []
    chimneys_inspections = []
    electrical_inspections = []
    heating_boiler_inspections = []
    air_conditioners_inspection = []

    fire_inspections = []

    buildings = Building.objects.all()
    for building in buildings:

        protocol_building_one = building.patterninspections.filter(inspection_name=1).order_by(
            "date_next_inspection").last()
        protocol_building_five = building.patterninspections.filter(inspection_name=2).order_by(
            "date_next_inspection").last()
        protocol_chimneys = building.patterninspections.filter(inspection_name=3).order_by(
            "date_next_inspection").last()
        protocol_electrical = building.patterninspections.filter(inspection_name=4).order_by(
            "date_next_inspection").last()
        protocol_heating_boiler = building.patterninspections.filter(inspection_name=5).order_by(
            "date_next_inspection").last()
        protocol_air_conditioners = building.patterninspections.filter(inspection_name=6).order_by(
            "date_next_inspection").last()
        protocol_fire = building.patterninspections.filter(inspection_name=6).order_by("date_next_inspection").last()

        if protocol_building_one != None and protocol_building_one.date_next_inspection < next_date:
            buildings_inspections_one_year.append(protocol_building_one)
            print(protocol_building_one.date_next_inspection)

        if protocol_building_five != None and protocol_building_five.date_next_inspection < next_date:
            buildings_inspections_five_year.append(protocol_building_five)

        if protocol_chimneys != None and protocol_chimneys.date_next_inspection < next_date:
            chimneys_inspections.append(protocol_chimneys)

        if protocol_electrical != None and protocol_electrical.date_next_inspection < next_date:
            electrical_inspections.append(protocol_electrical)

        if protocol_heating_boiler != None and protocol_heating_boiler.date_next_inspection < next_date:
            heating_boiler_inspections.append(protocol_heating_boiler)

        if protocol_air_conditioners != None and protocol_air_conditioners.date_next_inspection < next_date:
            air_conditioners_inspection.append(protocol_air_conditioners)

        if protocol_fire != None and protocol_fire.date_next_inspection < next_date:
            fire_inspections.append(protocol_fire)

    buildings_inspections_one_year_len = len(buildings_inspections_one_year)
    buildings_inspections_five_year_len = len(buildings_inspections_five_year)
    chimneys_inspections_len = len(chimneys_inspections)
    electrical_inspections_len = len(electrical_inspections)
    heating_boiler_inspections_len = len(heating_boiler_inspections)
    air_conditioners_inspection_len = len(air_conditioners_inspection)
    fire_inspections_len = len(fire_inspections)

    context = {"buildings_inspections_one_year": buildings_inspections_one_year[:3],
               "buildings_inspections_one_year_len": buildings_inspections_one_year_len,
               "buildings_inspections_five_year": buildings_inspections_five_year[:3],
               "buildings_inspections_five_year_len": buildings_inspections_five_year_len,
               "chimneys_inspections": chimneys_inspections, "chimneys_inspections_len": chimneys_inspections_len,
               "electricial_inspections": electrical_inspections[:3],
               "electrical_inspections_len": electrical_inspections_len,
               "air_conditioners_inspection": air_conditioners_inspection[:3],
               "air_conditioners_inspection_len": air_conditioners_inspection_len,
               "heating_boiler_inspections": heating_boiler_inspections[:3],
               "heating_boiler_inspections_len": heating_boiler_inspections_len,
               "fire_inspections": fire_inspections, "fire_inspections_len": fire_inspections_len}
    return render(request, "construction_inspections/priority_inspections.html", context)


@login_required
def buildings_inspections_choise(request):
    return render(request, "construction_inspections/buildings_choise_popup.html", {})


@login_required
def create_buildings_one_year_inspections(request):
    units = Unit.objects.all()
    context = {"units": units}
    return render(request, "construction_inspections/buildings_one_year_inspection.html", context)


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
