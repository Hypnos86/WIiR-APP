from django.shortcuts import render
from cpvdict.models import Typecpv
from cpvdict.forms import TypecpvForm


# Create your views here.
def cpvlist(request):
    cpvs = Typecpv.objects.all()
    query = "Wyczyść"
    search = "Szukaj"
    sumcpv = len(cpvs)
    q = request.GET.get("q")

    if q:
        cpvs = cpvs.filter(nocpv__startswith=q) | cpvs.filter(name__icontains=q)
        qsum = len(cpvs)
        return render(request, 'cpvdict/cpvlist.html', {'cpvs': cpvs,
                                                        'sumcpv': sumcpv, 'sumcpv': sumcpv, 'query': query,
                                                        'qsum': qsum, "q": q})
    else:
        return render(request, 'cpvdict/cpvlist.html', {'cpvs': cpvs,
                                                        'sumcpv': sumcpv, 'sumcpv': sumcpv, 'search': search})
