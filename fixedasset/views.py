from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from fixedasset.models import Building


# Create your views here.
@login_required
def fixed_asset_list(request):
    buildings = Building.objects.all().filter(state=True)
    buildings_sum = len(buildings)
    search = "Szukaj"
    query = "Wyczyść"

    paginator = Paginator(buildings, 30)
    page_number = request.GET.get('page')
    buildings_list = paginator.get_page(page_number)

    q = request.GET.get("q")

    if q:
        buildings = buildings.filter(no_inventory__icontains=q) \
                    | buildings.filter(building_name__icontains=q) \
                    | buildings.filter(unit__county__name__icontains=q) \
                    | buildings.filter(unit__city__icontains=q)

        buildings_sum = len(buildings)

        return render(request, "fixedasset/fixed_asset_list.html",
                      {"buildings": buildings, "buildings_sum": buildings_sum, "query": query})

    return render(request, "fixedasset/fixed_asset_list.html",
                  {"buildings": buildings_list, "buildings_sum": buildings_sum, "search": search})


@login_required
def show_information(request, id):
    building = get_object_or_404(Building, pk=id)
    return render(request, 'fixedasset/info_popup.html', {'building': building, 'id': id})
