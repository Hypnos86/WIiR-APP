from django.shortcuts import render, redirect, get_object_or_404
from .models import Contractor
from .forms import ContractorForm


def make_contractor_list(request):
    contractor = Contractor.objects.all()

    q = request.GET.get("q")
    if q:
        contractor = contractor.filter(miasto__icontains=q)
        return render(request, 'contractors/contractorslist.html', {'contractors': contractor})
    else:
        return render(request, 'contractors/contractorslist.html', {'contractors': contractor})


def make_new_contractor(request):
    contractor_form = ContractorForm(request.POST or None, request.FILES or None)

    if contractor_form.is_valid():
        contractor_form.save()
        # umowa_form.autor = request.user
        # umowa_form.save()
        # return HttpResponseRedirect(reversed("umowa_form/"))
        return redirect(make_contractor_list)
    return render(request, 'contractors/contractorform.html', {'contractor': contractor_form, 'new': True})


def edit_contractor(request, id):
    contractor_form = get_object_or_404(Contractor, pk=id)
    contractor_form = ContractorForm(request.POST or None, request.FILES or None)

    if contractor_form.is_valid():
        contractor_form.save()

        return redirect(make_contractor_list)

    return render(request, 'contractors/contractorform.html', {'contractor_form': contractor_form, 'new': False})
