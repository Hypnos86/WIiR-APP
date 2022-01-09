from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from cpvdict.models import Typecpv, Genre, OrderLimit, Order
from cpvdict.forms import OrderForm
from main.views import current_year
import datetime


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


@login_required
def type_expense_list(request):
    objects = Genre.objects.all().exclude(name_id="RB")
    limit = OrderLimit.objects.first()
    year = current_year()
    item = round(float(limit.limit) * 1.23, 2)

    context = {'objects': objects,
               'limit': limit,
               'item': item,
               'year': year}
    return render(request, 'cpvdict/genrelist.html', context)


@login_required
def type_work_list(request):
    objects_work = Order.objects.all().order_by("-date").filter(date__year=current_year())
    limit = OrderLimit.objects.first()
    year = current_year()
    item = round(float(limit.limit) * 1.23, 2)
    context = {'objects_work': objects_work,
               'limit': limit,
               'item': item,
               'year': year}
    return render(request, 'cpvdict/genreworklist.html', context)


@login_required
def order_list(request):
    orders = Order.objects.all().order_by("-date").filter(date__year=current_year())
    year = current_year()
    ordersum = len(orders)
    query = "Wyczyść"
    search = "Szukaj"
    q = request.GET.get("q")

    paginator = Paginator(orders, 30)
    page_number = request.GET.get('page')
    order_list = paginator.get_page(page_number)

    if q:
        orders = orders.filter(date__startswith=q) | orders.filter(no_order__icontains=q) | orders.filter(
            typeorder__type__icontains=q) | orders.filter(genre__name_id__icontains=q) | orders.filter(
            unit__powiat__powiat__icontains=q)
        return render(request, 'cpvdict/orderlist.html', {'orders': orders,
                                                          'year': year,
                                                          'ordersum': ordersum,
                                                          'query': query,
                                                          })
    else:
        return render(request, 'cpvdict/orderlist.html', {'orders': order_list,
                                                          'year': year,
                                                          'ordersum': ordersum,
                                                          'search': search
                                                          })


@login_required
def new_order(request):
    order_form = OrderForm(request.POST or None)

    if request.method == 'POST':

        if order_form.is_valid():
            instance = order_form.save(commit=False)
            instance.author = request.user
            instance.save()
            order_form.save()
            return redirect('cpvdict:order_list')
    return render(request, 'cpvdict/orderform.html', {'order_form': order_form, "new": True})
