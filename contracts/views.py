from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from contracts.models import Contractimmovables
from contracts.forms import ContractimmovablesForm


# Create your views here.
@login_required
def menu_contractsimmovables(request):
    contracts = Contractimmovables.objects.all().order_by("-data_umowy")
    query = "Wyczyść"
    search = "Szukaj"
    contrsum = len(contracts)

    q = request.GET.get("q")
    if q:
        contracts = contracts.filter(kontrahent__nazwa__icontains=q)
        return render(request, 'contracts/contractlist.html',
                      {'contracts': contracts, "contrsum": contrsum, "query": query})
    else:
        return render(request, 'contracts/contractlist.html',
                      {'contracts': contracts, "contrsum": contrsum, "search": search})


@login_required
def new_contractsimmovables(request):
    contract_form = ContractimmovablesForm(request.POST or None, request.FILES or None)
    context = {'contract_form': contract_form,
               'new': True}

    if request.method == 'POST':
        if contract_form.is_valid():
            instance = contract_form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect('contracts:menu_contractsimmovables')

    return render(request, 'contracts/contractform.html', context)


@login_required
def edit_contractsimmovables(request, id):
    contractsimmovables_edit = get_object_or_404(Contractimmovables, pk=id)
    contractsimmovables_form = ContractimmovablesForm(request.POST or None, request.FILES or None,
                                                      instance=contractsimmovables_edit)

    context = {'contract_form': contractsimmovables_form,
               'new': False}

    if contractsimmovables_form.is_valid():
        contractsimmovables_form.save()
        return redirect('contracts:menu_contractsimmovables')

    return render(request, 'contracts/contractform.html', context)
