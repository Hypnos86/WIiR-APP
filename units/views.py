from django.shortcuts import render
from .models import Jednostka


def make_units_list(request):
    units_act = Jednostka.objects.filter(aktywna=0)
    units_deact = Jednostka.objects.filter(aktywna=1)
    context = {"units": units_act,
               "units": units_deact}
    return render(request, "units/unitlist.html", context)
