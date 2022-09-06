from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
from datetime import date
from django.shortcuts import render, get_object_or_404
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspection, HeatingBoilerInspection, AirConditionerInspection, FireInspection, TypeInspection
# from constructioninspections.forms import AirConditionerInspectionForm
from fixedasset.models import Building


# Create your views here

@login_required
def important_inspections(request):
    next_date = date.today() + relativedelta(months=+2)
    print(next_date)

    buildings_inspections_one_year = []
    buildings_inspections_five_year = []
    chimneys_inspections = []
    electricial_inspections = []
    heating_boiler_inspections = []
    air_conditioners_inspection = []
    fire_inspections = []

    buildings_inspections_one_year_len = len(buildings_inspections_one_year)

    buildings = Building.objects.all()
    for building in buildings:
        print(building, end="\n")
        protocol = building.patterninspections.filter(date_next_inspection__range=[date.today(), next_date]).order_by("date_next_inspection").last()
        print(protocol)




    #     BuildingInspectionOneYear.objects.all().order_by("date_next_inspection")[:3]
    # buildings_inspections_one_year_date = BuildingInspectionOneYear.objects.all().order_by(
    #     "date_next_inspection").filter(date_next_inspection__range=[datetime.datetime.today(),next_date])
    # lenbuildings = len(buildings_inspections_one_year_date)
    # print(lenbuildings)

    # for next_building_inspection in buildings_inspections_one_year_date:
    #     print(next_building_inspection)
    #     # if next_building_inspection.date_next_inspection > next_date:
    #     #     print(list(next_building_inspection))

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
