''' Units render view '''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from units.models import Unit, County, TypeUnit
from units.forms import UnitForm


def units_list(request):
    units_active = Unit.objects.filter(status=1).order_by('county')

    county = County.objects.all().order_by("swop_id")
    type_unit = TypeUnit.objects.all()

    try:
        last_date = Unit.objects.values('change').latest('change')
    except Unit.DoesNotExist:
        last_date = None

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
                                                        'type_unit': type_unit,
                                                        'unit_sum': unit_sum,
                                                        'query': query,
                                                        'unit_sum_search': unit_sum_search,
                                                        'last_date': last_date,
                                                        'actual_units': True})
    elif p and not r:
        units_active = units_active.filter(county__exact=p)
        unit_sum_search = len(units_active)
        return render(request, "units/unit_list.html", {'units': units_active,
                                                        'county': county,
                                                        'type_unit': type_unit,
                                                        'unit_sum': unit_sum,
                                                        'query': query,
                                                        'unit_sum_search': unit_sum_search,
                                                        'last_date': last_date,
                                                        'actual_units': True})
    elif r and not p:
        units_active = units_active.filter(type__exact=r)
        unit_sum_search = len(units_active)
        return render(request, "units/unit_list.html", {'units': units_active,
                                                        'county': county,
                                                        'type_unit': type_unit,
                                                        'unit_sum': unit_sum,
                                                        'query': query,
                                                        'unit_sum_search': unit_sum_search,
                                                        'last_date': last_date,
                                                        'actual_units': True})

    else:
        return render(request, "units/unit_list.html", {'units': units_active,
                                                        'county': county,
                                                        'type_unit': type_unit,
                                                        'unit_sum': unit_sum,
                                                        'search': search,
                                                        'last_date': last_date,
                                                        'actual_units': True})


@login_required
def create_units_list_editable(request):
    units_active = Unit.objects.order_by('county')

    county = County.objects.all().order_by("swop_id")

    cities_objects = Unit.objects.all().values('id', 'city').filter(status=1)
    cities_set = set([city['city'] for city in cities_objects])
    cities = sorted(cities_set, reverse=False)

    type_unit = TypeUnit.objects.all()

    try:
        last_date = Unit.objects.values('change').latest('change')
    except Unit.DoesNotExist:
        last_date = None

    query = "Wyczyść"
    search = "Szukaj"
    unit_sum = len(units_active)

    r = request.GET.get("r")
    p = request.GET.get("p")
    c = request.GET.get("c")

    if p or c or r:

        if p:
            units_active = units_active.filter(county__exact=p)

        if c:
            units_active = units_active.filter(city__icontains=c)

        if r:
            units_active = units_active.filter(type__exact=r)

        unit_sum_search = len(units_active)
        return render(request, "units/unit_list_module.html", {'units': units_active,
                                                               'county': county,
                                                               'cities': cities,
                                                               'type_unit': type_unit,
                                                               'unit_sum': unit_sum,
                                                               'query': query,
                                                               'unit_sum_search': unit_sum_search,
                                                               'last_date': last_date,
                                                               'actual_units': True, 'r': r})

    else:
        return render(request, "units/unit_list_module.html", {'units': units_active,
                                                               'county': county,
                                                               'cities': cities,
                                                               'type_unit': type_unit,
                                                               'unit_sum': unit_sum,
                                                               'search': search,
                                                               'last_date': last_date,
                                                               'actual_units': True})


@login_required
def add_unit(request):
    unit_form = UnitForm(request.POST or None)

    if request.method == 'POST':
        if unit_form.is_valid():
            instance = unit_form.save(commit=False)
            instance.author = request.user
            unit_form.save()
            return redirect('units:create_units_list_editable')
    return render(request, 'units/unit_form.html', {'unit_form': unit_form, 'new': True})


@login_required
def edit_unit(request, id):
    unit_edit = get_object_or_404(Unit, pk=id)
    unit_form = UnitForm(request.POST or None, instance=unit_edit)

    if request.method == 'POST':
        if unit_form.is_valid():
            instance = unit_form.save(commit=False)
            instance.author = request.user
            unit_form.save()
            return redirect('units:create_units_list_editable')
    return render(request, 'units/unit_form.html', {'unit_form': unit_form, 'new': False})


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
