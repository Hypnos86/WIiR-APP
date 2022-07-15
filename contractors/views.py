from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Contractor
from .forms import ContractorsellForm


@login_required
def contractor_list(request):
    contractor = Contractor.objects.all().order_by("name")

    try:
        last_date = Contractor.objects.values('change').latest('change')
    except Contractor.DoesNotExist:
        last_date = None

    query = "Wyczyść"
    search = "Szukaj"
    contractor_len = len(contractor)
    q = request.GET.get("q")

    paginator = Paginator(contractor, 30)
    page_number = request.GET.get('page')
    contractor_list = paginator.get_page(page_number)

    if q:
        contractor = contractor.filter(name__icontains=q) \
                     | contractor.filter(city__icontains=q) \
                     | contractor.filter(no_contractor__startswith=q) \
                     | contractor.filter(nip__startswith=q)
        return render(request, 'contractors/contractor_list.html',
                      {'contractors': contractor, "consellsum": contractor_len, "query": query, 'last_date': last_date,
                       'q': q})
    else:
        return render(request, 'contractors/contractor_list.html',
                      {'contractors': contractor_list, "consellsum": contractor_len, "search": search,
                       'last_date': last_date})


@login_required
def show_information(request, id):
    contractor = get_object_or_404(Contractor, pk=id)
    return render(request, 'contractors/info_work_popup.html', {'contractor': contractor, 'id': id})


@login_required
def new_contractor(request):
    contractor_form = ContractorsellForm(request.POST or None)

    if request.method == 'POST':
        if contractor_form.is_valid():
            instance = contractor_form.save(commit=False)
            instance.author = request.user
            contractor_form.save()
            return redirect('contractors:contractor_list')
    return render(request, 'contractors/contractor_form.html',
                  {'contractor_form': contractor_form, "new": True})


@login_required
def edit_contractor(request, id):
    contractor_edit = get_object_or_404(Contractor, pk=id)
    contractor_form = ContractorsellForm(request.POST or None, instance=contractor_edit)

    context = {'contractor_form': contractor_form, 'new': False}

    if contractor_form.is_valid():
        contractor_form.save()
        return redirect('contractors:contractor_list')

    return render(request, 'contractors/contractor_form.html', context)
