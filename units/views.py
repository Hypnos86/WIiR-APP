import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from fixedasset.models import Building
from units.forms import UnitForm
from units.models import Unit, County, TypeUnit

logger = logging.getLogger(__name__)


class UnitListView(View):
    template = "units/unit_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units_active = Unit.objects.filter(status=1).order_by("county")

            county = County.objects.all().order_by("id_order")
            type_unit = TypeUnit.objects.all()

            try:
                last_date = Unit.objects.values("change").latest("change")
            except Unit.DoesNotExist:
                last_date = None

            query = "Wyczyść"
            search = "Szukaj"
            unit_sum = len(units_active)

            r = request.GET.get("r")
            p = request.GET.get("p")
            intP = None
            intR = None

            if p and r:
                units_active = units_active.filter(county__exact=p, type__exact=r)
                intR = int(r)
                intP = int(p)

                # print(units_active.type)
                unit_sum_search = len(units_active)
                context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
                           "query": query, "unit_sum_search": unit_sum_search, "last_date": last_date, "p": intP,
                           "r": intR,
                           "actual_units": True}
                return render(request, self.template, context)
            elif p and not r:
                units_active = units_active.filter(county__exact=p)
                intP = int(p)


                unit_sum_search = len(units_active)
                context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
                           "query": query, "unit_sum_search": unit_sum_search, "last_date": last_date, "p": intP,
                           "actual_units": True}
                return render(request, self.template, context)
            elif r and not p:
                units_active = units_active.filter(type__exact=r)
                intR = int(r)

                unit_sum_search = len(units_active)
                context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
                           "query": query, "unit_sum_search": unit_sum_search, "last_date": last_date, "r": intR,
                           "actual_units": True}
                return render(request, self.template, context)

            else:
                context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
                           "search": search, "last_date": last_date, "actual_units": True}
            return render(request, self.template, context)

        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class UnitsEditableListView(LoginRequiredMixin, View):
    template = "units/unit_list_module.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units_active = Unit.objects.order_by("county")

            county = County.objects.all().order_by("swop_id")

            cities_objects = Unit.objects.all().values("id", "city").filter(status=1)
            cities_set = set([city["city"] for city in cities_objects])
            cities = sorted(cities_set, reverse=False)

            type_unit = TypeUnit.objects.all()

            try:
                last_date = Unit.objects.values("change").latest("change")
            except Unit.DoesNotExist:
                last_date = None

            query = "Wyczyść"
            search = "Szukaj"
            unit_sum = len(units_active)

            p = request.GET.get("p")
            c = request.GET.get("c")
            r = request.GET.get("r")

            intP = None
            intR = None

            if p or c or r:

                if p:
                    units_active = units_active.filter(county__exact=p)
                    intP = int(p)

                if c:
                    units_active = units_active.filter(city__icontains=c)

                if r:
                    units_active = units_active.filter(type__exact=r)
                    intR = int(r)

                unit_sum_search = len(units_active)

                context = {"units": units_active, "county": county, "cities": cities, "type_unit": type_unit,
                           "unit_sum": unit_sum, "query": query, "unit_sum_search": unit_sum_search,
                           "last_date": last_date, "actual_units": True, "r": intR, "c": c, "p": intP}
                return render(request, self.template, context)

            else:
                context = {"units": units_active, "county": county, "cities": cities, "type_unit": type_unit,
                           "unit_sum": unit_sum, "search": search, "last_date": last_date, "actual_units": True}
                return render(request, self.template, context)

        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddUnitView(LoginRequiredMixin, View):
    template = "units/unit_form.html"
    template_error = 'main/error_site.html'
    form_class = UnitForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {"unit_form": form, "new": True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None)

            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.author = request.user
                    form.save()
                    return redirect("units:create_units_list_editable")
            return render(request, self.template, {"unit_form": form, "new": True})
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditUnitView(LoginRequiredMixin, View):
    template = "units/unit_form.html"
    template_error = 'main/error_site.html'

    def get(self, request, slug):
        try:
            unit_edit = get_object_or_404(Unit, slug=slug)
            unit_form = UnitForm(request.POST or None, instance=unit_edit)
            return render(request, self.template, {"unit_form": unit_form, "new": False})
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, slug):
        try:
            unit_edit = get_object_or_404(Unit, slug=slug)
            unit_form = UnitForm(request.POST or None, instance=unit_edit)
            if unit_form.is_valid():
                instance = unit_form.save(commit=False)
                instance.author = request.user
                unit_form.save()
                return redirect("units:create_units_list_editable")
            return render(request, self.template, {"unit_form": unit_form, "new": False})
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class UnitsArchiveListView(LoginRequiredMixin, View):
    template = "units/unit_list.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            units_archive = Unit.objects.filter(status=0).order_by("county")
            county = County.objects.all().order_by("swop_id")
            type_unit = TypeUnit.objects.all()
            query = "Wyczyść"
            search = "Szukaj"
            unit_sum = len(units_archive)

            r = request.GET.get("r")
            p = request.GET.get("p")

            if p and r:
                units_archive = units_archive.filter(county__exact=p, type__exact=r)
                unit_sum_search = len(units_archive)
                context = {"units_archive": units_archive, "county": county, "type_unit": type_unit,
                           "unit_sum": unit_sum,
                           "query": query, "unit_sum_search": unit_sum_search, "actual_units": False}
                return render(request, self.template, context)
            elif p and not r:
                units_archive = units_archive.filter(county__exact=p)
                unit_sum_search = len(units_archive)
                context = {"units_archive": units_archive, "county": county, "type_unit": type_unit,
                           "unit_sum": unit_sum,
                           "query": query, "unit_sum_search": unit_sum_search, "actual_units": False}
                return render(request, self.template, context)
            elif r and not p:
                units_archive = units_archive.filter(type__exact=r)
                unit_sum_search = len(units_archive)
                context = {"units_archive": units_archive, "county": county, "type_unit": type_unit,
                           "unit_sum": unit_sum,
                           "query": query, "unit_sum_search": unit_sum_search, "actual_units": False}
                return render(request, self.template, context)

            else:
                context = {"units_archive": units_archive, "county": county, "type_unit": type_unit,
                           "unit_sum": unit_sum, "search": search, "actual_units": False}
                return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowAllInfoUnit(LoginRequiredMixin, View):
    template = "units/unit_info.html"
    template_error = 'main/error_site.html'

    def get(self, request, slug, *args, **kwargs):
        try:
            unit_info = Unit.objects.get(slug=slug)
            orders = unit_info.order.all()
            projects = unit_info.project.all()
            donations = unit_info.application.all()
            contract_media = unit_info.contract_media.all().order_by("-state")
            contract_immovables = unit_info.contractimmovables.all()
            contract_auction = unit_info.contract_auction.all()
            buildings = unit_info.building.all()
            context = {"unit": unit_info, "orders": orders, "projects": projects, "donations": donations,
                       "contract_media": contract_media, "contract_immovables": contract_immovables,
                       "contract_auction": contract_auction, "buildings": buildings}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
