from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from invoices.models import Invoicesell
from invoices.forms import InvoicesellForm
from contractors.models import Contractor


# Create your views here.
@login_required
def menu_invoices(request):
    return render(request, 'invoices/invoicesmenu.html')


@login_required
def buy_invoiceslist(request):
    return render(request, 'invoices/invoicesbuylist.html')


@login_required
def sell_invoiceslist(request):
    invoicessell = Invoicesell.objects.all().order_by("-data")
    query = "Wyczyść"
    search = "Szukaj"
    invoicessellsum = len(invoicessell)
    q = request.GET.get("q")

    paginator = Paginator(invoicessell, 30)
    page_number = request.GET.get('page')
    invoicessell_list = paginator.get_page(page_number)

    if q:
        invoicessell = invoicessell.filter(noinvoice__icontains=q) | invoicessell.filter(
            sum__startswith=q) | invoicessell.filter(data__icontains=q) | invoicessell.filter(
            contractor__nazwa__icontains=q) | invoicessell.filter(
            contractor__nocuntractor__startswith=q) | invoicessell.filter(
            powiat__powiat__icontains=q)|invoicessell.filter(
            creator__creator__icontains=q)
        return render(request, "invoices/invoicesselllist.html", {"invoices": invoicessell,
                                                                  "invoicessellsum": invoicessellsum,
                                                                  "sell": True, "query": query})
    else:
        return render(request, "invoices/invoicesselllist.html", {"invoices": invoicessell_list,
                                                                  "invoicessellsum": invoicessellsum,
                                                                  "sell": True, "search": search})


@login_required
def new_invoicesell(request):
    invoicesell_form = InvoicesellForm(request.POST or None)
    context = {'invoicesell_form': invoicesell_form,
               'new': True}

    if request.method == 'POST':
        if invoicesell_form.is_valid():
            instance = invoicesell_form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect('invoices:sell_invoices_list')

    return render(request, 'invoices/invoicesellform.html', context)


@login_required
def edit_invoicesell(request, id):
    invoicesell_edit = get_object_or_404(Invoicesell, pk=id)
    invoicessell_form = InvoicesellForm(request.POST or None, instance=invoicesell_edit)

    context = {'invoicesell_form': invoicessell_form,
               'new': False}

    if invoicessell_form.is_valid():
        invoicesell_edit.save()
        return redirect('invoices:sell_invoices_list')

    return render(request, 'invoices/invoicesellform.html', context)
