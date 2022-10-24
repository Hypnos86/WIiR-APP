from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspectionOneYear, HeatingBoilerInspection, AirConditionerInspection, FireInspection, TypeInspection, \
    ElectricalInspectionFiveYear
from constructioninspections.forms import BuildingInspectionOneYearForm
from enum import Enum
from fixedasset.models import Building
from units.models import Unit


# Create your views here
class ProtocolType(Enum):
    overview_buildings_one_year = 1
    overview_buildings_five_year = 2
    overview_chimney = 3
    overview_electrical_one_year = 4
    overview_electrical_five_year = 5
    overview_heating_boilers = 6
    overview_air_conditioners = 7
    overview_fire_inspection = 8


@login_required
def important_inspections(request):
    next_date = date.today() + relativedelta(months=+3)

    buildings_inspections_one_year = []
    # buildings_inspections_one_year.sort()
    buildings_inspections_five_year = []
    # buildings_inspections_five_year.sort()
    chimneys_inspections = []
    electrical_inspections_one_year = []
    electrical_inspections_five_year = []
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

        protocol_electrical_one = building.patterninspections.filter(inspection_name=4).order_by(
            "date_next_inspection").last()

        protocol_electrical_five = building.patterninspections.filter(inspection_name=5).order_by(
            "date_next_inspection").last()

        protocol_heating_boiler = building.patterninspections.filter(inspection_name=6).order_by(
            "date_next_inspection").last()

        protocol_air_conditioners = building.patterninspections.filter(inspection_name=7).order_by(
            "date_next_inspection").last()

        protocol_fire = building.patterninspections.filter(inspection_name=8).order_by("date_next_inspection").last()

        if protocol_building_one != None and protocol_building_one.date_next_inspection < next_date:
            buildings_inspections_one_year.append(protocol_building_one)

        if protocol_building_five != None and protocol_building_five.date_next_inspection < next_date:
            buildings_inspections_five_year.append(protocol_building_five)

        if protocol_chimneys != None and protocol_chimneys.date_next_inspection < next_date:
            chimneys_inspections.append(protocol_chimneys)

        if protocol_electrical_one != None and protocol_electrical_one.date_next_inspection < next_date:
            electrical_inspections_one_year.append(protocol_electrical_one)

        if protocol_electrical_five != None and protocol_electrical_five.date_next_inspection < next_date:
            electrical_inspections_five_year.append(protocol_electrical_five)

        if protocol_heating_boiler != None and protocol_heating_boiler.date_next_inspection < next_date:
            heating_boiler_inspections.append(protocol_heating_boiler)

        if protocol_air_conditioners != None and protocol_air_conditioners.date_next_inspection < next_date:
            air_conditioners_inspection.append(protocol_air_conditioners)

        if protocol_fire != None and protocol_fire.date_next_inspection < next_date:
            fire_inspections.append(protocol_fire)

    buildings_inspections_one_year_len = len(buildings_inspections_one_year)
    buildings_inspections_five_year_len = len(buildings_inspections_five_year)
    chimneys_inspections_len = len(chimneys_inspections)
    electrical_inspections_one_len = len(electrical_inspections_one_year)
    electrical_inspections_five_len = len(electrical_inspections_five_year)
    heating_boiler_inspections_len = len(heating_boiler_inspections)
    air_conditioners_inspection_len = len(air_conditioners_inspection)
    fire_inspections_len = len(fire_inspections)

    context = {"buildings_inspections_one_year": buildings_inspections_one_year[:3],
               "buildings_inspections_one_year_len": buildings_inspections_one_year_len,
               "buildings_inspections_five_year": buildings_inspections_five_year[:3],
               "buildings_inspections_five_year_len": buildings_inspections_five_year_len,
               "chimneys_inspections": chimneys_inspections[:3],
               "chimneys_inspections_len": chimneys_inspections_len,
               "electrical_inspections_one_year": electrical_inspections_one_year[:3],
               "electrical_inspections_one_len": electrical_inspections_one_len,
               "electrical_inspections_five_year": electrical_inspections_five_year[:3],
               "electrical_inspections_five_len": electrical_inspections_five_len,
               "air_conditioners_inspection": air_conditioners_inspection[:3],
               "air_conditioners_inspection_len": air_conditioners_inspection_len,
               "heating_boiler_inspections": heating_boiler_inspections[:3],
               "heating_boiler_inspections_len": heating_boiler_inspections_len,
               "fire_inspections": fire_inspections, "fire_inspections_len": fire_inspections_len}
    return render(request, "construction_inspections/priority_inspections.html", context)


@login_required
def buildings_inspections_choice(request):
    return render(request, "construction_inspections/buildings_choice_popup.html", {})


@login_required
def electrical_inspections_choice(request):
    return render(request, "construction_inspections/electrical_choice_popup.html", {})


@login_required
def create_buildings_one_year_inspections_list(request):
    units = Unit.objects.all()
    context = {"units": units, "overview": ProtocolType.overview_buildings_one_year}
    return render(request, "construction_inspections/buildings_one_year_inspection.html", context)


@login_required
def create_buildings_five_year_inspections_list(request):
    context = {"overview": ProtocolType.overview_buildings_five_year}
    return render(request, "construction_inspections/buildings_five_year_inspection.html", context)


@login_required
def create_chimney_inspection_list(request):
    objects = ChimneyInspection.objects.all()
    context = {"objects": objects, "overview": ProtocolType.overview_chimney}
    return render(request, "construction_inspections/chimneys_inspection_list.html", context)


@login_required
def create_electrical_inspection_one_year_list(request):
    objects = ElectricalInspectionOneYear.objects.all()
    context = {"objects": objects, "overview": ProtocolType.overview_electrical_one_year}
    return render(request, "construction_inspections/electrical_inspection_one_year_list.html", context)


@login_required
def create_electrical_inspection_five_year_list(request):
    objects = ElectricalInspectionFiveYear.objects.all()
    context = {"objects": objects, "overview": ProtocolType.overview_electrical_five_year}
    return render(request, "construction_inspections/electrical_inspection_five_year_list.html", context)


@login_required
def create_heating_boilers_inspection_list(request):
    objects = HeatingBoilerInspection.objects.all()
    context = {"objects": objects, "overview": ProtocolType.overview_heating_boilers}
    return render(request, "construction_inspections/heating_boilers_inspection_list.html", context)


@login_required
def create_air_conditioners_inspection_list(request):
    objects = AirConditionerInspection.objects.all()
    context = {"objects": objects, "overview": ProtocolType.overview_air_conditioners}
    return render(request, "construction_inspections/air_conditioners_inspection_list.html", context)


@login_required
def create_fire_inspection_list(request):
    objects = FireInspection.objects.all()
    context = {"objects": objects, "overview": ProtocolType.overview_fire_inspection}
    return render(request, "construction_inspections/fire_inspection_list.html", context)


@login_required
def add_protocol(request, typeInspection):
    protocol_form = BuildingInspectionOneYearForm(request.POST or None)
    if typeInspection == ProtocolType.overview_buildings_one_year.name:
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_buildings_one_year.value)
    elif typeInspection == "overview_buildings_five_year":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_buildings_five_year.value)
    elif typeInspection == "overview_chimney":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_chimney.value)
    elif typeInspection == "overview_electrical_one_year":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_electrical_one_year.value)
    elif typeInspection == "overview_electrical_five_year":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_electrical_five_year.value)
    elif typeInspection == "overview_heating_boilers":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_heating_boilers.value)
    elif typeInspection == "overview_air_conditioners":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_air_conditioners.value)
    elif typeInspection == "overview_fire_inspection":
        typeProtocol = TypeInspection.objects.get(pk=ProtocolType.overview_fire_inspection.value)

    print(typeProtocol.id)

    if request.method == "POST":
        if protocol_form.is_valid():
            instance = protocol_form.save(commit=False)
            instance.author = request.user
            protocol_form.save()
            return redirect("constructioninspections:create_buildings_one_year_inspections_list")
    return render(request, "construction_inspections/protocol_inspection_form.html",
                  {"form": protocol_form, "new": True, "typeProtocol": typeProtocol})
