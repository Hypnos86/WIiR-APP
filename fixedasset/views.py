from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from fixedasset.models import Building
from fixedasset.forms import BuildingForm
from units.models import Unit


# Create your views here.
@login_required
def fixed_asset_list(request):
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

        return render(request, "fixedasset/fixed_asset_list.html",
                      {"buildings": buildings, "buildings_sum": buildings_sum, "buildings_search": buildings_search,
                       "buildings_sum_all": buildings_sum_all, "query": query})

    return render(request, "fixedasset/fixed_asset_list.html",
                  {"buildings": buildings_list, "buildings_sum": buildings_sum, "buildings_sum_all": buildings_sum_all,
                   "search": search})


@login_required
def show_information(request, id):
    building = get_object_or_404(Building, pk=id)
    return render(request, 'fixedasset/info_popup.html', {'building': building, 'id': id})


@login_required
def add_new_building(request):
    building_form = BuildingForm(request.POST or None)
    units = Unit.objects.all().order_by("county__id_order")

    if request.method == "POST":
        if building_form.is_valid():
            instance = building_form.save(commit=False)
            instance.author = request.user
            building_form.save()
            return redirect("fixedasset:fixed_asset_list")
    return render(request, "fixedasset/fixed_asset_form.html",
                  {"building_form": building_form, "units": units, "new": True})


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
