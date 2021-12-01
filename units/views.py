from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from units.models import Jednostka
from units.forms import JednotkskaForm


def make_units_list(request):
    units_act = Jednostka.objects.filter(aktywna=0)
    units_deact = Jednostka.objects.filter(aktywna=1)
    context = {"units": units_act,
               "units": units_deact}
    return render(request, "units/unitlist.html", context)


def make_new_unit(request):
    unit_form = JednotkskaForm(request.POST or None)

    if request.method == 'POST':
        if unit_form.is_valid():
            unit_form.save()
        return redirect(make_units_list)
    return render(request, "units/unitform.html", {"unit_form": unit_form})
