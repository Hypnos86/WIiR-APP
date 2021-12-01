from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contractor
from .forms import ContractorForm


def contractor_list(request):
    contractor = Contractor.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    q = request.GET.get("q")
    if q:
        contractor = contractor.filter(nazwa__icontains=q)
        return render(request, 'contractors/contractorslist.html', {'contractors': contractor, "query": query})
    else:
        return render(request, 'contractors/contractorslist.html', {'contractors': contractor, "search": search})


def make_new_contractor(request):
    contractor_form = ContractorForm(request.POST or None)

    if request.method == 'POST':

        if contractor_form.is_valid():
            instance = contractor_form.save(commit=False)
            instance.autor = request.user
            instance.save()
            contractor_form.save()
            return redirect(contractor_list)
    return render(request, 'contractors/contractorform.html', {'contractor_form': contractor_form, "new": True})


def edit_contractor(request, id):
    contractor_edit = get_object_or_404(Contractor, pk=id)
    contractor_form = ContractorForm(request.POST or None, instance=contractor_edit)

    if contractor_form.is_valid():
        contractor_form.save()
        return redirect(contractor_list)

    return render(request, 'contractors/contractorform.html', {'contractor_form': contractor_form, "new": False})
