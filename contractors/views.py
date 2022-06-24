from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Contractor
from .forms import ContractorsellForm


@login_required
def contractorsell_list(request):
    contractorsell = Contractor.objects.all().order_by("name")

    try:
        last_date = Contractor.objects.values('change').latest('change')
    except Contractor.DoesNotExist:
        last_date = None

    query = "Wyczyść"
    search = "Szukaj"
    consellsum = len(contractorsell)
    q = request.GET.get("q")

    paginator = Paginator(contractorsell, 30)
    page_number = request.GET.get('page')
    contractorsell_list = paginator.get_page(page_number)

    if q:
        contractorsell = contractorsell.filter(name__icontains=q) | contractorsell.filter(
            city__icontains=q) | contractorsell.filter(no_contractor__startswith=q) | contractorsell.filter(
            nip__startswith=q)
        return render(request, 'contractors/contractor_list.html',
                      {'contractors': contractorsell, "consellsum": consellsum, "query": query, 'last_date': last_date})
    else:
        return render(request, 'contractors/contractor_list.html',
                      {'contractors': contractorsell_list, "consellsum": consellsum, "search": search,
                       'last_date': last_date})


@login_required
def show_information(request, id):
    contractor = get_object_or_404(Contractor, pk=id)
    return render(request, 'contractors/information_popup.html', {'contractor': contractor, 'id': id})


@login_required
def new_contractorsell(request):
    contractorsell_form = ContractorsellForm(request.POST or None)

    if request.method == 'POST':
        if contractorsell_form.is_valid():
            instance = contractorsell_form.save(commit=False)
            instance.author = request.user
            instance.save()
            contractorsell_form.save()
            return redirect('contractors:contractorssell_list')
    return render(request, 'contractors/contractor_form.html',
                  {'contractor_form': contractorsell_form, "new": True})


@login_required
def edit_contractorsell(request, id):
    contractorsell_edit = get_object_or_404(Contractor, pk=id)
    contractorsell_form = ContractorsellForm(request.POST or None, instance=contractorsell_edit)

    context = {'contractor_form': contractorsell_form, 'new': False}

    if contractorsell_form.is_valid():
        contractorsell_form.save()
        return redirect('contractors:contractorssell_list')

    return render(request, 'contractors/contractor_form.html', context)
