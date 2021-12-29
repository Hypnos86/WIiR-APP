from django.shortcuts import render
from cpvdict.models import Typecpv, OrderingObject
from cpvdict.forms import TypecpvForm


# Create your views here.
def cpvlist(request):
    cpvs = Typecpv.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    sumcpv = len(cpvs)
    q = request.GET.get("q")

    if q:
        cpvs = cpvs.filter(no_cpv__startswith=q) | cpvs.filter(name__icontains=q)
        qsum = len(cpvs)
        return render(request, 'cpvdict/cpvlist.html', {'cpvs': cpvs,
                                                        'sumcpv': sumcpv, 'query': query,
                                                        'qsum': qsum, "q": q})
    else:
        return render(request, 'cpvdict/cpvlist.html', {'cpvs': cpvs,
                                                        'sumcpv': sumcpv, 'search': search})


def type_expense_list(request):
    objects = OrderingObject.objects.all()
    context = {'objects': objects}
    return render(request, 'cpvdict/typelist.html', context)
