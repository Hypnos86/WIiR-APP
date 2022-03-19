''' Units render view '''
from django.shortcuts import render, redirect
from units.models import Unit, Powiat, UnitKind
from units.forms import UnitForm


def units_list(request):
    units_active = Unit.objects.filter(aktywna=1).order_by("powiat")
    units_deact = Unit.objects.filter(aktywna=0)
    powiaty = Powiat.objects.all().order_by("swop_id")
    rodzaje = UnitKind.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    unitsum = len(units_active)

    r = request.GET.get("r")
    p = request.GET.get("p")

    if p and r:
        units_active = units_active.filter(powiat__exact=p, unit_kind__exact=r)
        unitsumsearch = len(units_active)
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "powiaty": powiaty,
                                                       "rodzaje": rodzaje,
                                                       "unitsum": unitsum, "query": query,
                                                       "unitsumsearch": unitsumsearch})
    elif p and not r:
        units_active = units_active.filter(powiat__exact=p)
        unitsumsearch = len(units_active)
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "powiaty": powiaty,
                                                       "rodzaje": rodzaje,
                                                       "unitsum": unitsum, "query": query,
                                                       "unitsumsearch": unitsumsearch})
    elif r and not p:
        units_active = units_active.filter(unit_kind__exact=r)
        unitsumsearch = len(units_active)
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "powiaty": powiaty,
                                                       "rodzaje": rodzaje,
                                                       "unitsum": unitsum, "query": query,
                                                       "unitsumsearch": unitsumsearch})

    else:
        return render(request, "units/unitlist.html", {"units": units_active,
                                                       "powiaty": powiaty,
                                                       "rodzaje": rodzaje,
                                                       "unitsum": unitsum, "search": search})


def add_unit(request):
    unit_form = UnitForm(request.POST or None)

    if request.method == 'POST':
        if unit_form.is_valid():
            unit_form.save()
            return redirect('units:units_list')
    return render(request, "units/unitform.html", {"unit_form": unit_form})
