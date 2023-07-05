from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from fixedasset.models import Building
from fixedasset.forms import BuildingForm
from units.models import Unit


# Create your views here.
class FixedAssetListView(LoginRequiredMixin, View):
    template = "fixedasset/list_fixed_asset.html"

    def get(self, request):
        buildings_all = Building.objects.all().order_by("-unit__county__name")
        buildings_actual = Building.objects.all().filter(state=True)
        buildings_sum = len(buildings_actual)
        buildings_sum_all = len(buildings_all)
        search = "Szukaj"
        query = "Wyczyść"

        paginator = Paginator(buildings_all, 30)
        page_number = request.GET.get('page')
        buildings_list = paginator.get_page(page_number)

        q = request.GET.get("q")

        if q:
            buildings = buildings_all.filter(no_inventory__icontains=q) \
                        | buildings_all.filter(kind__kind__icontains=q) \
                        | buildings_all.filter(building_name__icontains=q) \
                        | buildings_all.filter(unit__county__name__icontains=q) \
                        | buildings_all.filter(unit__city__icontains=q) \
                        | buildings_all.filter(unit__address__icontains=q)

            buildings_search = len(buildings)
            context = {"buildings": buildings, "buildings_sum": buildings_sum, "buildings_search": buildings_search,
                       "buildings_sum_all": buildings_sum_all, "query": query}
            return render(request, self.template, context)

        context = {"buildings": buildings_list, "buildings_sum": buildings_sum, "buildings_sum_all": buildings_sum_all,
                   "search": search}
        return render(request, self.template, context)


class ShowInformationView(LoginRequiredMixin, View):
    template = "fixedasset/info_popup.html"

    def get(self, request, id):
        building = get_object_or_404(Building, pk=id)
        context = {'building': building, 'id': id}
        return render(request, self.template, context)


class AddBuildingView(LoginRequiredMixin, View):
    template = "fixedasset/fixed_asset_form.html"
    units = Unit.objects.all().order_by("county__id_order")
    form_class = BuildingForm

    def get(self, request):
        form = self.form_class()
        context = {"building_form": form, "units": self.units, "new": True}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form_class(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect("fixedasset:fixed_asset_list")
        context = {"building_form": form, "units": self.units, "new": True}
        return render(request, self.template, context)


@login_required
def edit_building(request, id):
    building = get_object_or_404(Building, pk=id)
    building_form = BuildingForm(request.POST or None, instance=building)
    units = Unit.objects.all()
    unit_edit = building

    if request.method == "POST":
        if building_form.is_valid():
            instance = building_form.save(commit=False)
            instance.author = request.user
            building_form.save()
            return redirect("fixedasset:fixed_asset_list")
    return render(request, "fixedasset/fixed_asset_form.html",
                  {"building_form": building_form, "units": units, "unit_edit": unit_edit, "new": False})
