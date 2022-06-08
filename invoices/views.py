from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from invoices.models import InvoiceSell, Creator, InvoiceBuy
from invoices.forms import InvoiceSellForm, InvoiceBuyForm
from main.views import current_year, year_choises


# Create your views here.
@login_required
def menu_invoices(request):
    now_year = current_year()
    all_year = year_choises()
    return render(request, 'invoices/invoices_menu.html', {"now_year": now_year, "all_year": all_year})


@login_required
def buy_invoices_list(request):
    invoices_buy = InvoiceBuy.objects.all().order_by("-date_receipt").filter(date_receipt__year=current_year())
    query = "Wyczyść"
    search = "Szukaj"
    invoices_buy_sum = len(invoices_buy)
    year = current_year()
    q = request.GET.get("q")

    paginator = Paginator(invoices_buy, 40)
    page_number = request.GET.get('page')
    invoices_buy_list = paginator.get_page(page_number)

    if q:
        invoicesbuy = invoices_buy.filter(no_invoice__icontains=q) | invoices_buy.filter(
            sum__startswith=q) | invoices_buy.filter(contractor__name__icontains=q) | invoices_buy.filter(
            contractor__no_contractor__startswith=q) | invoices_buy.filter(
            invoiceitems__county__name__icontains=q)
        invoices_buy_filter_sum = len(invoicesbuy)
        return render(request, 'invoices/invoices_buy_list.html', {"invoices": invoicesbuy,
                                                                   "invoices_buy_sum": invoices_buy_filter_sum,
                                                                   "query": query, "year": year,
                                                                   })
    else:
        return render(request, 'invoices/invoices_buy_list.html', {"invoices": invoices_buy_list,
                                                                   "invoices_buy_sum": invoices_buy_sum,
                                                                   "search": search, "year": year,
                                                                   })


@login_required
def show_info_buy(request, id):
    invoice = get_object_or_404(InvoiceBuy, pk=id)
    return render(request, 'invoices/info_buy_popup.html', {'invoice': invoice, 'id': id})


@login_required
def new_invoice_buy(request):
    invoice_buy_form = InvoiceBuyForm(request.POST or None)
    context = {'invoice': invoice_buy_form, 'new': True}

    if request.method == 'POST':
        if invoice_buy_form.is_valid():
            instance = invoice_buy_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('invoices:buy_invoices_list')
    return render(request, 'invoices/invoice_buy_form.html', context)


@login_required
def edit_invoice_buy(request, id):
    invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
    invoice_buy_form = InvoiceBuyForm(request.POST or None, instance=invoice_buy_edit)

    context = {'invoice': invoice_buy_form,
               'new': False}

    if invoice_buy_form.is_valid():
        instance = invoice_buy_form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('invoices:buy_invoices_list')

    return render(request, 'invoices/invoice_buy_form.html', context)


@login_required
def sell_invoices_list(request):
    invoicessell = InvoiceSell.objects.all().order_by("-date").filter(date__year=current_year())
    query = "Wyczyść"
    search = "Szukaj"
    invoicessellsum = len(invoicessell)
    year = current_year()
    creators = Creator.objects.all()
    q = request.GET.get("q")

    paginator = Paginator(invoicessell, 40)
    page_number = request.GET.get('page')
    invoicessell_list = paginator.get_page(page_number)

    if q:
        invoicessell = invoicessell.filter(no_invoice__icontains=q) | invoicessell.filter(
            sum__startswith=q) | invoicessell.filter(date__startswith=q) | invoicessell.filter(
            contractor__name__icontains=q) | invoicessell.filter(
            contractor__no_contractor__startswith=q) | invoicessell.filter(
            county__name__icontains=q) | invoicessell.filter(
            creator__creator__icontains=q)
        invoices_sell_filter_sum = len(invoicessell)
        return render(request, "invoices/invoices_sell_list.html", {"invoices": invoicessell,
                                                                    "invoicessellsum": invoices_sell_filter_sum,
                                                                    "query": query, "year": year,
                                                                    "creators": creators})
    else:
        return render(request, "invoices/invoices_sell_list.html", {"invoices": invoicessell_list,
                                                                    "invoicessellsum": invoicessellsum,
                                                                    "search": search, "year": year,
                                                                    "creators": creators})


@login_required
def show_info_sell(request, id):
    invoice = get_object_or_404(InvoiceSell, pk=id)
    return render(request, 'invoices/info_sell_popup.html', {'invoice': invoice, 'id': id})


@login_required
def new_invoice_sell(request):
    invoice_sell_form = InvoiceSellForm(request.POST or None)
    context = {'invoice': invoice_sell_form, 'new': True}

    if request.method == 'POST':
        if invoice_sell_form.is_valid():
            instance = invoice_sell_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('invoices:sell_invoices_list')
    return render(request, 'invoices/invoice_sell_form.html', context)


@login_required
def edit_invoice_sell(request, id):
    invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
    invoice_sell_form = InvoiceSellForm(request.POST or None, instance=invoice_sell_edit)

    context = {'invoice': invoice_sell_form,
               'new': False}

    if invoice_sell_form.is_valid():
        instance = invoice_sell_form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('invoices:sell_invoices_list')
    return render(request, 'invoices/invoice_sell_form.html', context)


@login_required
def make_verification(request):
    invoices_buy = InvoiceBuy.objects.all().order_by("date_of_payment")
    query = "Wyczyść"
    search = "Szukaj"

    year = current_year()
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    if date_from and date_to:
        invoicesbuy = invoices_buy.filter(date_of_payment__range=[date_from, date_to])
        invoices_buy_sum = len(invoicesbuy)
        return render(request, 'invoices/verification.html', {'invoices': invoicesbuy,
                                                              'invoices_buy_sum': invoices_buy_sum,
                                                              'query': query, 'year': year,
                                                              'date_from': date_from,
                                                              'date_to': date_to})
    else:
        invoices_buy_sum = 0
        return render(request, 'invoices/verification.html', {
            "invoices_buy_sum": invoices_buy_sum,
            "search": search, "year": year,
        })
