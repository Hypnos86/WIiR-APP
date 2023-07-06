from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal

from django.views import View

from cpvdict.models import Typecpv, Genre, OrderLimit, Order
from cpvdict.forms import OrderForm
from main.views import current_year
from units.models import Unit
from main.models import Employer


class CpvDictionary(View):
    template = "cpvdict/dictionary.html"

    def get(self, request):
        cpvs = Typecpv.objects.all()
        query = "Wyczyść"
        search = "Szukaj"
        sumcpv = len(cpvs)
        q = request.GET.get("q")

        if q:
            cpvs = cpvs.filter(no_cpv__startswith=q) | cpvs.filter(name__icontains=q)
            qsum = len(cpvs)
            context = {'cpvs': cpvs, 'sumcpv': sumcpv, 'query': query, 'qsum': qsum, "q": q}
            return render(request, self.template, context)
        else:
            context = {'cpvs': cpvs, 'sumcpv': sumcpv, 'search': search}
            return render(request, self.template, context)


class GenericMenu(LoginRequiredMixin, View):
    template = "cpvdict/generic_menu.html"

    def get(self, request):
        year = current_year()
        genres = Genre.objects.all().exclude(name_id="RB")

        try:
            limit = OrderLimit.objects.get(year=year)
            limit_netto = limit.limit_netto
            limit_item = round(limit_netto, 2)
        except ObjectDoesNotExist:
            limit = year
            limit_netto = 0
            limit_item = round(limit_netto, 2)

        for object in genres:
            order_genre = Order.objects.all().filter(genre=object).filter(date__year=current_year()).filter(
                brakedown=False)
            sum = 0
            for order in order_genre:
                sum += order.sum_netto

            object.sum_netto = Decimal(sum)
            object.remain = round(limit_item - object.sum_netto, 2)

        context = {'objects': genres, 'limit': limit_netto, 'limit_item': limit_item, 'year': year}
        return render(request, self.template, context)


class ConstructionWorksClassificationListView(LoginRequiredMixin, View):
    template = "cpvdict/genre_work_list.html"

    def get(self, request):
        year = current_year()
        units = Unit.objects.all()
        try:
            limit = OrderLimit.objects.get(year=year)
            limit_netto = limit.limit_netto
        except ObjectDoesNotExist:
            limit = year
            limit_netto = 0

        sum_rb = {}
        for unit in units:
            orders = Order.objects.all().filter(genre__name_id='RB').filter(unit=unit).filter(date__year=current_year())
            sum = 0
            for order in orders:
                sum += order.sum_netto
            sum_rb[unit] = sum

        year = current_year()

        context = {'units': units, 'limit': limit, 'year': year, 'sum_rb': sum_rb}
        return render(request, self.template, context)


class ShowInfoWorkObject(LoginRequiredMixin, View):
    template = "cpvdict/info_work_popup.html"

    def get(self, request, id, year):
        work_object = get_object_or_404(Unit, pk=id)
        orders = Order.objects.all().filter(date__year=year).filter(genre__name_id='RB').filter(unit__id=id).order_by(
            'date')
        context = {'work_object': work_object, 'orders': orders, 'id': id, 'year': year}
        return render(request, self.template, context)


class OrderListView(LoginRequiredMixin, View):
    template = "cpvdict/order_list.html"

    def get(self, request):
        orders = Order.objects.all().order_by("-date").filter(date__year=current_year())
        year = current_year()
        ordersum = len(orders)
        query = "Wyczyść"
        search = "Szukaj"
        q = request.GET.get("q")
        date_from = request.GET.get('from', None)
        date_to = request.GET.get('to', None)

        paginator = Paginator(orders, 30)
        page_number = request.GET.get('page')
        order_list = paginator.get_page(page_number)

        if q or date_from or date_to:
            if q:
                orders = orders.filter(date__startswith=q) \
                         | orders.filter(no_order__icontains=q) \
                         | orders.filter(typeorder__type__icontains=q) \
                         | orders.filter(genre__name_id__icontains=q) \
                         | orders.filter(unit__county__name__icontains=q) \
                         | orders.filter(unit__city__icontains=q) \
                         | orders.filter(unit__address__icontains=q) \
                         | orders.filter(contractor__name__icontains=q)

            if date_from:
                orders = orders.filter(date__gte=date_from)
            if date_to:
                orders = orders.filter(date__lte=date_to)

            ordersum = len(orders)
            context = {'orders': set(orders), 'year': year, 'ordersum': ordersum, 'query': query, 'q': q,
                       'date_from': date_from, 'date_to': date_to}
            return render(request, self.template, context)
        else:
            context = {'orders': order_list, 'year': year, 'ordersum': ordersum, 'search': search}
            return render(request, self.template, context)


class ShowOrderInfo(LoginRequiredMixin, View):
    template = "cpvdict/order_info_popup.html"

    def get(self, request, id):
        order = get_object_or_404(Order, pk=id)
        context = {'order': order, 'id': id}
        return render(request, self.template, context)


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
                  {'order_form': order_form, 'unit_edit': unit_edit, 'order_edit': order_edit, 'new': False,
                   'units': units})


class ArchiveYearListView(LoginRequiredMixin, View):
    template = "cpvdict/archive_list_year_order_popup.html"

    def get(self, request):
        now_year = current_year()
        all_year_order = Order.objects.all().values('date__year').exclude(date__year=now_year)
        year_order_set = set([year['date__year'] for year in all_year_order])
        year_order_list = sorted(year_order_set, reverse=True)
        context = {'now_year': now_year, 'year_order_list': year_order_list}
        return render(request, self.template, context)


class OrderArchiveListView(LoginRequiredMixin, View):
    template = "cpvdict/archive_order_list.html"

    def get(self, request, year):
        orders = Order.objects.all().order_by("-date").filter(date__year=year)
        ordersum = len(orders)
        query = "Wyczyść"
        search = "Szukaj"
        q = request.GET.get("q")
        date_from = request.GET.get('from', None)
        date_to = request.GET.get('to', None)

        paginator = Paginator(orders, 30)
        page_number = request.GET.get('page')
        order_list = paginator.get_page(page_number)

        if q or date_from or date_to:
            if q:
                orders = orders.filter(date__startswith=q) \
                         | orders.filter(no_order__icontains=q) \
                         | orders.filter(typeorder__type__icontains=q) \
                         | orders.filter(genre__name_id__icontains=q) \
                         | orders.filter(unit__county__name__icontains=q) \
                         | orders.filter(unit__city__icontains=q) \
                         | orders.filter(unit__address__icontains=q) \
                         | orders.filter(contractor__name__icontains=q)

            if date_from:
                orders = orders.filter(date__gte=date_from)
            if date_to:
                orders = orders.filter(date__lte=date_to)

            ordersum = len(orders)
            context = {'orders': set(orders), 'year': year, 'ordersum': ordersum, 'query': query, 'q': q,
                       'date_from': date_from, 'date_to': date_to}
            return render(request, self.template, context)
        else:
            context = {'orders': order_list, 'year': year, 'ordersum': ordersum, 'search': search}
            return render(request, self.template, context)


class ConstructionWorksArchiveList(LoginRequiredMixin, View):
    template = "cpvdict/archive_genre_work_list.html"
    units = Unit.objects.all()

    def get(self, request, year):
        sum_rb = {}
        for unit in self.units:
            orders = Order.objects.all().filter(brakedown=False).filter(genre__name_id='RB').filter(unit=unit).filter(
                date__year=year)
            sum = 0
            for order in orders:
                sum += order.sum_netto
            sum_rb[unit] = sum

        try:
            limit = OrderLimit.objects.get(year=year)
        except ObjectDoesNotExist:
            limit = year
        context = {'units': self.units, 'limit': limit, 'year': year, 'sum_rb': sum_rb}
        return render(request, self.template, context)


class GenreArchiveView(LoginRequiredMixin, View):
    template = "cpvdict/archive_genre_tree.html"

    def get(self, request, year):
        objects = Genre.objects.all().exclude(name_id="RB")

        try:
            limit = OrderLimit.objects.get(year=year)
            limit_netto = limit.limit_netto
            limit_item = round(limit_netto, 2)
        except ObjectDoesNotExist:
            limit_netto = 0
            limit_item = round(limit_netto, 2)

        for object in objects:
            order_genre = Order.objects.all().filter(genre=object).filter(date__year=year).filter(brakedown=False)
            sum = 0
            for order in order_genre:
                sum += order.sum_netto

            object.sum_netto = Decimal(sum)
            try:
                object.remain = round(limit_item - object.sum_netto, 2)
            except UnboundLocalError:
                object.remain = round(object.sum_netto, 2)

        context = {'objects': objects,
                   'limit': limit_netto,
                   'year': year}
        return render(request, self.template, context)
