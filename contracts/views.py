from django.shortcuts import render
from contracts.models import Contractimmovables


# Create your views here.
def menu_contractsimmovables(request):
    contracts = Contractimmovables.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    contrsum = len(contracts)

    q = request.GET.get("q")
    if q:
        contracts = contracts.filter(nazwa__icontains=q)
        return render(request, 'contracts/contractlist.html',
                      {'contracts': contracts, "consellsum": contrsum, "query": query})
    else:
        return render(request, 'contracts/contractlist.html',
                      {'contracts': contracts, "consellsum": contrsum, "search": search})


def new_contractsimmovables(request):
    context = {}
    return render(request, 'contracts/newcontract.html', context)


def edit_contractsimmovables(request):
    context = {}
    return render(request, 'contracts/editcontract.html', context)
