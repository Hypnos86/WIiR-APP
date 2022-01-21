from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from invoices.models import Invoicesell, Creator
from invoices.forms import InvoicesellForm
from main.views import current_year, year_choises
import datetime


# Create your views here.
@login_required
def menu_invoices(request):
    now_year = current_year()
    all_year = year_choises()
    return render(request, 'invoices/invoices_menu.html', {"now_year": now_year, "all_year": all_year})


@login_required
def buy_invoiceslist(request):
    return render(request, 'invoices/invoices_buy_list.html')


@login_required
def sell_invoiceslist(request):
    invoicessell = Invoicesell.objects.all().order_by("-data").filter(data__year=current_year())
    query = "Wyczyść"
    search = "Szukaj"
    invoicessellsum = len(invoicessell)
    year = current_year()
    creators = Creator.objects.all()
    q = request.GET.get("q")

    paginator = Paginator(invoicessell, 30)
    page_number = request.GET.get('page')
    invoicessell_list = paginator.get_page(page_number)

    if q:
        invoicessell = invoicessell.filter(noinvoice__icontains=q) | invoicessell.filter(
            sum__startswith=q) | invoicessell.filter(data__startswith=q) | invoicessell.filter(
            contractor__nazwa__icontains=q) | invoicessell.filter(
            contractor__nocuntractor__startswith=q) | invoicessell.filter(
            powiat__powiat__icontains=q) | invoicessell.filter(
            creator__creator__icontains=q)
        return render(request, "invoices/invoicessell_list.html", {"invoices": invoicessell,
                                                                  "invoicessellsum": invoicessellsum,
                                                                  "sell": True, "query": query, "year": year,
                                                                  "creators": creators})
    else:
        return render(request, "invoices/invoicessell_list.html", {"invoices": invoicessell_list,
                                                                  "invoicessellsum": invoicessellsum,
                                                                  "sell": True, "search": search, "year": year,
                                                                  "creators": creators})


@login_required
def new_invoicesell(request):
    invoicesell_form = InvoicesellForm(request.POST or None)
    context = {'invoicesell_form': invoicesell_form,
               'new': True}

    if request.method == 'POST':
        if invoicesell_form.is_valid():
            instance = invoicesell_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('invoices:sell_invoices_list')

    return render(request, 'invoices/invoicesell_form.html', context)


@login_required
def edit_invoicesell(request, id):
    invoicesell_edit = get_object_or_404(Invoicesell, pk=id)
    invoicessell_form = InvoicesellForm(request.POST or None, instance=invoicesell_edit)

    context = {'invoicesell_form': invoicessell_form,
               'new': False}

    if invoicessell_form.is_valid():
        invoicesell_edit.save()
        return redirect('invoices:sell_invoices_list')

    return render(request, 'invoices/invoicesell_form.html', context)
