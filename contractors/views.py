from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contractorsell, Contractorbuy
from .forms import ContractorsellForm


def contractorsell_list(request):
    contractorsell = Contractorsell.objects.all().order_by("nazwa")
    query = "Wyczyść"
    search = "Szukaj"
    consellsum = len(contractorsell)
    q = request.GET.get("q")
    if q:
        contractorsell = contractorsell.filter(nazwa__icontains=q)
        return render(request, 'contractors/contractorsselllist.html',
                      {'contractors': contractorsell, "consellsum": consellsum, "query": query})
    else:
        return render(request, 'contractors/contractorsselllist.html',
                      {'contractors': contractorsell, "consellsum": consellsum, "search": search})


def new_contractorsell(request):
    contractorsell_form = ContractorsellForm(request.POST or None)

    if request.method == 'POST':

        if contractorsell_form.is_valid():
            instance = contractorsell_form.save(commit=False)
            instance.autor = request.user
            instance.save()
            contractorsell_form.save()
            return redirect('contractors:contractorssell_list')
    return render(request, 'contractors/contractorsellform.html', {'contractor_form': contractorsell_form, "new": True})


def edit_contractorsell(request, id):
    contractorsell_edit = get_object_or_404(Contractorsell, pk=id)
    contractorsell_form = ContractorsellForm(request.POST or None, instance=contractorsell_edit)

    if contractorsell_form.is_valid():
        contractorsell_form.save()
        return redirect('contractors:contractorssell_list')

    return render(request, 'contractors/contractorsellform.html',
                  {'contractor_form': contractorsell_form, "new": False})
