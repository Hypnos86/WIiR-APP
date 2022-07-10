from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from decimal import *
from cpvdict.models import Typecpv, Genre, OrderLimit, Order
from cpvdict.forms import OrderForm
from main.views import current_year
from units.models import Unit
from main.models import Employer
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
        return render(request, 'cpvdict/cpv_list.html', {'cpvs': cpvs,
                                                         'sumcpv': sumcpv, 'query': query,
                                                         'qsum': qsum, "q": q})
    else:
        return render(request, 'cpvdict/cpv_list.html', {'cpvs': cpvs,
                                                         'sumcpv': sumcpv, 'search': search})


@login_required
def type_expense_list(request):
    objects = Genre.objects.all().exclude(name_id="RB")
    limit = OrderLimit.objects.first()
    limit_item = round(limit.limit_netto * Decimal(1.23), 2)

    for object in objects:
        order_genre = Order.objects.all().filter(genre=object).filter(date__year=current_year()).filter(brakedown=False)
        sum = 0
        for order in order_genre:
            sum += order.sum_netto

        object.sum_netto = Decimal(sum)
        object.remain = round(limit_item - object.sum_netto, 2)

    year = current_year()

    context = {'objects': objects,
               'limit': limit.limit_netto,
               'limit_item': limit_item,
               'year': year}
    return render(request, 'cpvdict/genre_list.html', context)


@login_required
def type_work_list(request):
    units = Unit.objects.all()
    limit = OrderLimit.objects.first()

    sum_rb = {}
    for unit in units:
        orders = Order.objects.all().filter(genre__name_id='RB').filter(unit=unit).filter(date__year=current_year())
        sum = 0
        for order in orders:
            sum += order.sum_netto
        sum_rb[unit] = sum

    year = current_year()
    item = round(float(limit.limit_netto) * 1.23, 2)

    context = {'units': units, 'limit': limit, 'item': item, 'year': year, 'sum_rb': sum_rb}
    return render(request, 'cpvdict/genre_work_list.html', context)


@login_required
def show_information_work_object(request, id):
    work_object = get_object_or_404(Unit, pk=id)
    return render(request, 'cpvdict/information_popup.html', {'work_object': work_object, 'id': id})


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
            unit__county__name__icontains=q) | orders.filter(unit__city__icontains=q) | orders.filter(
            unit__address__icontains=q) | orders.filter(contractor__name__icontains=q)
        return render(request, 'cpvdict/order_list.html',
                      {'orders': orders, 'year': year, 'ordersum': ordersum, 'query': query
                       })
    else:
        return render(request, 'cpvdict/order_list.html',
                      {'orders': order_list, 'year': year, 'ordersum': ordersum, 'search': search
                       })


@login_required
def show_order_info_popup(request, id):
    order = get_object_or_404(Order, pk=id)
    return render(request, 'cpvdict/order_info_popup.html', {'order': order, 'id': id})


@login_required
def new_order(request):
    order_form = OrderForm(request.POST or None)
    order_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all()

    if request.method == 'POST':

        if order_form.is_valid():
            instance = order_form.save(commit=False)
            instance.author = request.user
            instance.save()
            order_form.save()
            return redirect('cpvdict:order_list')
    return render(request, 'cpvdict/order_form.html', {'order_form': order_form, 'new': True, 'units': units})


@login_required
def edit_order(request, id):
    order_edit = get_object_or_404(Order, pk=id)
    order_form = OrderForm(request.POST or None, request.FILES or None, instance=order_edit)
    order_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all()
    unit_edit = order_edit.unit

    if request.method == "POST":
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.author = request.user
            order_form.save()
            return redirect('cpvdict:order_list')
    return render(request, 'cpvdict/order_form.html',
                  {'order_form': order_form, 'unit_edit': unit_edit, 'new': False, 'units': units})
