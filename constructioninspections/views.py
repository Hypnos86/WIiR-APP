import logging
from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, ChimneyInspection, \
    ElectricalInspectionOneYear, HeatingBoilerInspection, AirConditionerInspection, FireInspection, TypeInspection, \
    ElectricalInspectionFiveYear
from constructioninspections.forms import BuildingInspectionOneYearForm, BuildingInspectionFiveYearForm, \
    ElectricalInspectionOneYearForm, ElectricalInspectionFiveYearForm, FireInspectionForm, ChimneyInspectionForm, \
    AirConditionerInspectionForm, HeatingBoilerInspectionForm
from enum import Enum
from fixedasset.models import Building
from units.models import Unit
from main.views import now_date

logger = logging.getLogger(__name__)


# Create your views here
class ProtocolType(Enum):
    OVERVIEW_BUILDINGS_ONE_YEAR = [1, "Przeglądy jednoroczne budynków"]
    OVERVIEW_BUILDINGS_FIVE_YEAR = [2, "Przeglądy pięcioletnie budynków"]
    OVERVIEW_CHIMNEYS = [3, "Przeglądy kominów"]
    OVERVIEW_ELECTRICAL_ONE_YEAR = [4, "Przeglądy jednoroczne instalacji elektrycznej"]
    OVERVIEW_ELECTRICAL_FIVE_YEAR = [5, "Przeglądy pięcioletnie instalacji elektrycznej"]
    OVERVIEW_HEATING_BOILERS = [6, "Przeglądy kotłów grzewczych"]
    OVERVIEW_AIR_CONDITIONERS = [7, "Przeglądy klimatyzatorów"]
    OVERVIEW_FIRE_INSPECTION = [8, "Przeglądy przeciwpożarowe"]


class ImportantInspections(LoginRequiredMixin, View):
    template = "construction_inspections/priority_inspections.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            staticMonths = 3
            next_date = date.today() + relativedelta(months=+staticMonths)
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

                protocol_building_one = building.building_inspection_one_year.filter(
                    inspection_name=ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_building_five = building.building_inspection_five_year.filter(
                    inspection_name=ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_chimneys = building.chimney_inspection.filter(
                    inspection_name=ProtocolType.OVERVIEW_CHIMNEYS.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_electrical_one = building.electrical_inspection_one_year.filter(
                    inspection_name=ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_electrical_five = building.electrical_inspection_five_year.filter(
                    inspection_name=ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_heating_boiler = building.heating_boiler_inspection.filter(
                    inspection_name=ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_air_conditioners = building.air_conditioner_inspection.filter(
                    inspection_name=ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]).order_by(
                    "date_next_inspection").last()

                protocol_fire = building.fire_inspection.filter(
                    inspection_name=ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]).order_by(
                    "date_next_inspection").last()

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
                       "fire_inspections": fire_inspections, "fire_inspections_len": fire_inspections_len,
                       "staticMonths": staticMonths}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class BuildingsInspectionsChoice(LoginRequiredMixin, View):
    template = "construction_inspections/buildings_choice_popup.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            return render(request, self.template, {})
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ElectricalInspectionsChoice(LoginRequiredMixin, View):
    template = "construction_inspections/electrical_choice_popup.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            return render(request, self.template, {})
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class BuildingsOneYearInspectionsList(LoginRequiredMixin, View):
    template = "construction_inspections/buildings_one_year_inspection.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class BuildingsFiveYearInspectionsList(LoginRequiredMixin, View):
    template = "construction_inspections/buildings_five_year_inspection.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ChimneyInspectionList(LoginRequiredMixin, View):
    template = "construction_inspections/chimneys_inspection_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_CHIMNEYS.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_CHIMNEYS.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ElectricalInspectionOneYearList(LoginRequiredMixin, View):
    template = "construction_inspections/electrical_inspection_one_year_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ElectricalInspectionFiveYearList(LoginRequiredMixin, View):
    template = "construction_inspections/electrical_inspection_five_year_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class HeatingBoilersInspectionList(LoginRequiredMixin, View):
    template = "construction_inspections/heating_boilers_inspection_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_HEATING_BOILERS.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AirConditionersInspectionList(LoginRequiredMixin, View):
    template = "construction_inspections/air_conditioners_inspection_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class FireInspectionList(LoginRequiredMixin, View):
    template = "construction_inspections/fire_inspection_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units = Unit.objects.all().order_by("county__id_order")
            typeInspection = ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]
            context = {"units": units, "overview": ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0],
                       "typeInspection": typeInspection}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddProtocolView(View):
    template = "construction_inspections/protocol_inspection_form.html"
    template_error = 'main/error_site.html'

    def get(self, request, typeInspection, id=None):
        try:
            typeProtocol = None
            protocol_form = None
            redirectText = None

            if typeInspection == ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0])
                protocol_form = BuildingInspectionOneYearForm(request.POST or None)
                redirectText = "constructioninspections:create_buildings_one_year_inspections_list"

            elif typeInspection == ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0])
                protocol_form = BuildingInspectionFiveYearForm(request.POST or None)
                redirectText = "constructioninspections:create_buildings_five_year_inspections_list"

            elif typeInspection == ProtocolType.OVERVIEW_CHIMNEYS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_CHIMNEYS.value[0])
                protocol_form = ChimneyInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_chimney_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0])
                protocol_form = ElectricalInspectionOneYearForm(request.POST or None)
                redirectText = "constructioninspections:create_electrical_inspection_one_year_list"

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0])
                protocol_form = ElectricalInspectionFiveYearForm(request.POST or None)
                redirectText = "constructioninspections:create_electrical_inspection_five_year_list"

            elif typeInspection == ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_HEATING_BOILERS.value[0])
                protocol_form = HeatingBoilerInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_heating_boilers_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0])
                protocol_form = AirConditionerInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_air_conditioners_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0])
                protocol_form = FireInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_fire_inspection_list"

            context = {"form": protocol_form,
                       "new": True,
                       "typeProtocol": typeProtocol}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, typeInspection, id=None):
        try:
            typeProtocol = None
            protocol_form = None
            redirectText = None

            if typeInspection == ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0])
                protocol_form = BuildingInspectionOneYearForm(request.POST or None)
                redirectText = "constructioninspections:create_buildings_one_year_inspections_list"

            elif typeInspection == ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0])
                protocol_form = BuildingInspectionFiveYearForm(request.POST or None)
                redirectText = "constructioninspections:create_buildings_five_year_inspections_list"

            elif typeInspection == ProtocolType.OVERVIEW_CHIMNEYS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_CHIMNEYS.value[0])
                protocol_form = ChimneyInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_chimney_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0])
                protocol_form = ElectricalInspectionOneYearForm(request.POST or None)
                redirectText = "constructioninspections:create_electrical_inspection_one_year_list"

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0])
                protocol_form = ElectricalInspectionFiveYearForm(request.POST or None)
                redirectText = "constructioninspections:create_electrical_inspection_five_year_list"

            elif typeInspection == ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_HEATING_BOILERS.value[0])
                protocol_form = HeatingBoilerInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_heating_boilers_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0])
                protocol_form = AirConditionerInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_air_conditioners_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0])
                protocol_form = FireInspectionForm(request.POST or None)
                redirectText = "constructioninspections:create_fire_inspection_list"

            if protocol_form.is_valid():
                instance = protocol_form.save(commit=False)
                instance.author = request.user
                protocol_form.save()
                return redirect(redirectText)

            context = {
                "form": protocol_form,
                "new": True,
                "typeProtocol": typeProtocol
            }
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditProtocolView(View):
    template = "construction_inspections/protocol_inspection_form.html"
    template_error = 'main/error_site.html'

    def get_object_form(self, request, typeInspection, id):
        try:
            if typeInspection == ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0])
                object = get_object_or_404(BuildingInspectionOneYear, pk=id)
                protocol_form = BuildingInspectionOneYearForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_buildings_one_year_inspections_list"

            elif typeInspection == ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0])
                object = get_object_or_404(BuildingInspectionFiveYear, pk=id)
                protocol_form = BuildingInspectionFiveYearForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_buildings_five_year_inspections_list"

            elif typeInspection == ProtocolType.OVERVIEW_CHIMNEYS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_CHIMNEYS.value[0])
                object = get_object_or_404(ChimneyInspection, pk=id)
                protocol_form = ChimneyInspectionForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_chimney_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0])
                object = get_object_or_404(ElectricalInspectionOneYear, pk=id)
                protocol_form = ElectricalInspectionOneYearForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_electrical_inspection_one_year_list"

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0])
                object = get_object_or_404(ElectricalInspectionFiveYear, pk=id)
                protocol_form = ElectricalInspectionFiveYearForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_electrical_inspection_five_year_list"

            elif typeInspection == ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_HEATING_BOILERS.value[0])
                object = get_object_or_404(HeatingBoilerInspection, pk=id)
                protocol_form = HeatingBoilerInspectionForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_heating_boilers_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0])
                object = get_object_or_404(AirConditionerInspection, pk=id)
                protocol_form = AirConditionerInspectionForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_air_conditioners_inspection_list"

            elif typeInspection == ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]:
                typeProtocol = get_object_or_404(TypeInspection, pk=ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0])
                object = get_object_or_404(FireInspection, pk=id)
                protocol_form = FireInspectionForm(request.POST or None, instance=object)
                redirectText = "constructioninspections:create_fire_inspection_list"

            return typeProtocol, object, protocol_form, redirectText
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def get(self, request, typeInspection, id):
        try:
            typeProtocol, object, protocol_form, redirectText = self.get_object_form(request, typeInspection, id)
            context = {"form": protocol_form,
                       "new": False,
                       "typeProtocol": typeProtocol,
                       "redirectText": redirectText}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, typeInspection, id):
        try:
            typeProtocol, object, protocol_form, redirectText = self.get_object_form(request, typeInspection, id)
            if protocol_form.is_valid():
                instance = protocol_form.save(commit=False)
                instance.author = request.user
                protocol_form.save()
                return redirect(redirectText)
            context = {"form": protocol_form,
                       "new": False,
                       "typeProtocol": typeProtocol,
                       "redirectText": redirectText}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowInformationProtocolView(LoginRequiredMixin, View):
    template = "construction_inspections/info_popup.html"
    template_error = 'main/error_site.html'

    def get(self, request, typeInspection, id):
        try:
            if typeInspection == ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]:
                protocol = BuildingInspectionOneYear.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]:
                protocol = BuildingInspectionFiveYear.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_CHIMNEYS.value[0]:
                protocol = ChimneyInspection.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_CHIMNEYS.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]:
                protocol = ElectricalInspectionOneYear.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]:
                protocol = ElectricalInspectionFiveYear.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]:
                protocol = HeatingBoilerInspection.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]:
                protocol = AirConditionerInspection.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]

            elif typeInspection == ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]:
                protocol = FireInspection.objects.get(pk=id)
                overview = ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]

            context = {"typeInspection": typeInspection, "id": id, "protocol": protocol, "overview": overview}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class PriorityInspectionsList(LoginRequiredMixin, View):
    template = "construction_inspections/priority_inspections_list.html"
    template_error = 'main/error_site.html'
    now = now_date

    def get(self, request, typeInspection):
        try:
            setMonths = request.GET.get("setMonth")
            if setMonths == None:
                setMonths = 3
            else:
                setMonths = int(setMonths)

            next_date = date.today() + relativedelta(months=+setMonths)
            priority_inspection = []
            title = None
            buildings = Building.objects.all()

            for building in buildings:

                if typeInspection == ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]:
                    title = ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[1]
                    protocol_building_one = building.building_inspection_one_year.filter(
                        inspection_name=ProtocolType.OVERVIEW_BUILDINGS_ONE_YEAR.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_building_one != None and protocol_building_one.date_next_inspection < next_date:
                        priority_inspection.append(protocol_building_one)

                elif typeInspection == ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]:
                    title = ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[1]
                    protocol_building_five = building.building_inspection_five_year.filter(
                        inspection_name=ProtocolType.OVERVIEW_BUILDINGS_FIVE_YEAR.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_building_five != None and protocol_building_five.date_next_inspection < next_date:
                        priority_inspection.append(protocol_building_five)

                elif typeInspection == ProtocolType.OVERVIEW_CHIMNEYS.value[0]:
                    title = ProtocolType.OVERVIEW_CHIMNEYS.value[1]
                    protocol_chimneys = building.chimney_inspection.filter(
                        inspection_name=ProtocolType.OVERVIEW_CHIMNEYS.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_chimneys != None and protocol_chimneys.date_next_inspection < next_date:
                        priority_inspection.append(protocol_chimneys)

                elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]:
                    title = ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[1]
                    protocol_electrical_one = building.electrical_inspection_one_year.filter(
                        inspection_name=ProtocolType.OVERVIEW_ELECTRICAL_ONE_YEAR.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_electrical_one != None and protocol_electrical_one.date_next_inspection < next_date:
                        priority_inspection.append(protocol_electrical_one)

                elif typeInspection == ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]:
                    title = ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[1]
                    protocol_electrical_five = building.electrical_inspection_five_year.filter(
                        inspection_name=ProtocolType.OVERVIEW_ELECTRICAL_FIVE_YEAR.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_electrical_five != None and protocol_electrical_five.date_next_inspection < next_date:
                        priority_inspection.append(protocol_electrical_five)

                elif typeInspection == ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]:
                    title = ProtocolType.OVERVIEW_HEATING_BOILERS.value[1]
                    protocol_heating_boiler = building.heating_boiler_inspection.filter(
                        inspection_name=ProtocolType.OVERVIEW_HEATING_BOILERS.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_heating_boiler != None and protocol_heating_boiler.date_next_inspection < next_date:
                        priority_inspection.append(protocol_heating_boiler)

                elif typeInspection == ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]:
                    title = ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[1]
                    protocol_air_conditioners = building.air_conditioner_inspection.filter(
                        inspection_name=ProtocolType.OVERVIEW_AIR_CONDITIONERS.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_air_conditioners != None and protocol_air_conditioners.date_next_inspection < next_date:
                        priority_inspection.append(protocol_air_conditioners)

                elif typeInspection == ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]:
                    title = ProtocolType.OVERVIEW_FIRE_INSPECTION.value[1]
                    protocol_fire = building.fire_inspection.filter(
                        inspection_name=ProtocolType.OVERVIEW_FIRE_INSPECTION.value[0]).order_by(
                        "date_next_inspection").last()
                    if protocol_fire != None and protocol_fire.date_next_inspection < next_date:
                        priority_inspection.append(protocol_fire)

            priority_inspection_len = len(priority_inspection)

            context = {"priority_inspection": priority_inspection, "priority_inspection_len": priority_inspection_len,
                       "title": title, "setMonths": setMonths, "typeInspection": typeInspection, "now": self.now}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
