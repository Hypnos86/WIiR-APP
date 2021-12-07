from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from units.models import Unit, Powiat, Rodzaj
from units.forms import UnitForm


def units_list(request):
    units_act = Unit.objects.filter(aktywna=1).order_by("powiat")
    units_deact = Unit.objects.filter(aktywna=0)
    powiaty = Powiat.objects.all().order_by("powiat")
    rodzaj = Rodzaj.objects.all()

    context = {"units": units_act,
               "powiaty": powiaty,
               "rodzaj":rodzaj}
    return render(request, "units/unitlist.html", context)


def add_unit(request):
    unit_form = UnitForm(request.POST or None)

    if request.method == 'POST':
        if unit_form.is_valid():
            unit_form.save()
            return redirect('units:units_list')
    return render(request, "units/unitform.html", {"unit_form": unit_form})
