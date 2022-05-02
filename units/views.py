''' Units render view '''
from django.shortcuts import render, redirect
from units.models import Unit, County, TypeUnit
from units.forms import UnitForm


def units_list(request):
    units_active = Unit.objects.filter(status=1).order_by('county')
    units_archive = Unit.objects.filter(status=0).order_by('county')
    county = County.objects.all().order_by("swop_id")
    type_unit = TypeUnit.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    unit_sum = len(units_active)

    r = request.GET.get("r")
    p = request.GET.get("p")

    if p and r:
        units_active = units_active.filter(county__exact=p, type__exact=r)
        unit_sum_search = len(units_active)
        return render(request, "units/unit_list.html", {'units': units_active,
                                                        'county': county,
                                                        "type_unit": type_unit,
                                                        "unit_sum": unit_sum,
                                                        "query": query,
                                                        "unit_sum_search": unit_sum_search,
                                                        'actual_units': True})
    elif p and not r:
        units_active = units_active.filter(county__exact=p)
        unit_sum_search = len(units_active)
        return render(request, "units/unit_list.html", {"units": units_active,
                                                        "county": county,
                                                        "type_unit": type_unit,
                                                        "unit_sum": unit_sum,
                                                        "query": query,
                                                        "unit_sum_search": unit_sum_search,
                                                        'actual_units': True})
    elif r and not p:
        units_active = units_active.filter(type__exact=r)
        unit_sum_search = len(units_active)
        return render(request, "units/unit_list.html", {"units": units_active,
                                                        "county": county,
                                                        "type_unit": type_unit,
                                                        "unit_sum": unit_sum,
                                                        "query": query,
                                                        "unit_sum_search": unit_sum_search,
                                                        'actual_units': True})

    else:
        return render(request, "units/unit_list.html", {"units": units_active,
                                                        "county": county,
                                                        "type_unit": type_unit,
                                                        "unit_sum": unit_sum,
                                                        "search": search,
                                                        'actual_units': True})


def add_unit(request):
    unit_form = UnitForm(request.POST or None)

    if request.method == 'POST':
        if unit_form.is_valid():
            unit_form.save()
            return redirect('units:units_list')
    return render(request, "units/unitform.html", {"unit_form": unit_form})


def archive_units_list(request):
    units_archive = Unit.objects.filter(status=0).order_by('county')
    county = County.objects.all().order_by("swop_id")
    type_unit = TypeUnit.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    unit_sum = len(units_archive)

    r = request.GET.get("r")
    p = request.GET.get("p")

    if p and r:
        units_archive = units_archive.filter(county__exact=p, type__exact=r)
        unit_sum_search = len(units_archive)
        return render(request, "units/unit_list.html", {'units_archive': units_archive,
                                                            'county': county,
                                                            "type_unit": type_unit,
                                                            "unit_sum": unit_sum,
                                                            "query": query,
                                                            "unit_sum_search": unit_sum_search,
                                                            'actual_units': False})
    elif p and not r:
        units_archive = units_archive.filter(county__exact=p)
        unit_sum_search = len(units_archive)
        return render(request, "units/unit_list.html", {"units_archive": units_archive,
                                                            "county": county,
                                                            "type_unit": type_unit,
                                                            "unit_sum": unit_sum,
                                                            "query": query,
                                                            "unit_sum_search": unit_sum_search,
                                                            'actual_units': False})
    elif r and not p:
        units_archive = units_archive.filter(type__exact=r)
        unit_sum_search = len(units_archive)
        return render(request, "units/unit_list.html", {"units_archive": units_archive,
                                                            "county": county,
                                                            "type_unit": type_unit,
                                                            "unit_sum": unit_sum,
                                                            "query": query,
                                                            "unit_sum_search": unit_sum_search,
                                                            'actual_units': False})

    else:
        return render(request, "units/unit_list.html", {"units_archive": units_archive,
                                                            "county": county,
                                                            "type_unit": type_unit,
                                                            "unit_sum": unit_sum,
                                                            "search": search,
                                                            'actual_units': False})
