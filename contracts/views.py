from django.shortcuts import render, redirect
from contracts.models import Contractimmovables
from contracts.forms import ContractimmovablesForm


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
                      {'contracts': contracts, "contrsum": contrsum, "query": query})
    else:
        return render(request, 'contracts/contractlist.html',
                      {'contracts': contracts, "contrsum": contrsum, "search": search})


def new_contractsimmovables(request):
    contract_form = ContractimmovablesForm(request.POST or None)
    context = {'contract_form': contract_form}
    if request.method != 'POST':
        if contract_form.is_valid():
            contract_form.save()
            return redirect('contracts:menu_contractsimmovables')

    return render(request, 'contracts/contractedit.html', context)


def edit_contractsimmovables(request):
    context = {}
    return render(request, 'contracts/editcontract.html', context)
