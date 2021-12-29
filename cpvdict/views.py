from django.shortcuts import render
from cpvdict.models import Typecpv, Genre, Order
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
    objects = Genre.objects.all().exclude(name_id="RB")
    context = {'objects': objects}
    return render(request, 'cpvdict/genrelist.html', context)


def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'cpvdict/orderlist.html', context)
