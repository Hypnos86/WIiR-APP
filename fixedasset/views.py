from django.shortcuts import render
from fixedasset.models import Building


# Create your views here.
def fixed_asset_list(request):
    buildings = Building.objects.all().filter(state=True)
    buildings_sum = len(buildings)
    search = "Szukaj"
    query = "Wyczyść"

    q = request.GET.get("q")

    return render(request, "fixedasset/fixed_asset_list.html",
                  {"buildings": buildings, "buildings_sum": buildings_sum, "search": search, "query": query})
