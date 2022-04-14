''' Units render view '''
from django.shortcuts import render, redirect
from units.models import Unit, County, TypeUnit
from units.forms import UnitForm


def units_list(request):
    units_active = Unit.objects.filter(status=1).order_by('county')
    units_deactivate = Unit.objects.filter(status=0)
    county = County.objects.all().order_by("swop_id")
    type_unit = TypeUnit.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    unit_sum = len(units_active)

    r = request.GET.get("r")
    p = request.GET.get("p")

    if p and r:
        units_active = units_active.filter(powiat__exact=p, rodzaj__exact=r)
        unit_sum_search = len(units_active)
        return render(request, "units/unitlist.html", {'units': units_active,
                                                       'county': county,
                                                       "type_unit": type_unit,
                                                       "unit_sum": unit_sum, "query": query,
                                                       "unit_sum_search": unit_sum_search})
    elif p and not r:
        units_active = units_active.filter(powiat__exact=p)
        unit_sum_search = len(units_active)
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "county": county,
                                                       "type_unit": type_unit,
                                                       "unit_sum": unit_sum, "query": query,
                                                       "unit_sum_search": unit_sum_search})
    elif r and not p:
        units_active = units_active.filter(rodzaj__exact=r)
        unit_sum_search = len(units_active)
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "county": county,
                                                       "type_unit": type_unit,
                                                       "unit_sum": unit_sum, "query": query,
                                                       "unit_sum_search": unit_sum_search})

    else:
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "county": county,
                                                       "type_unit": type_unit,
                                                       "unit_sum": unit_sum, "search": search})


def add_unit(request):
    unit_form = UnitForm(request.POST or None)

    if request.method == 'POST':
        if unit_form.is_valid():
            unit_form.save()
            return redirect('units:units_list')
    return render(request, "units/unitform.html", {"unit_form": unit_form})
