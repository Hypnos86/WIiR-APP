from django.shortcuts import render, redirect
from invoices.models import Invoicesell
from invoices.forms import InvoicesellForm


# Create your views here.
def menu_invoices(request):
    return render(request, 'invoices/invoicesmenu.html')


def buy_invoiceslist(request):
    return render(request, 'invoices/invoicesbuylist.html')


def sell_invoiceslist(request):
    invoicessell = Invoicesell.objects.all().order_by("data")
    invoicessellsum = len(invoicessell)
    context = {"invoices": invoicessell,
               "invoicessellsum": invoicessellsum,
               "sell": True}
    return render(request, "invoices/invoicesselllist.html", context)

# def sell_invoiceslist(request):
#     invoice = InvoicesellForm(request.POST or None)
#     context = {"invoice_form": invoice}
#     if request.method == "POST":
#         if invoice.is_valid():
#             invoice.save()
#         return redirect("invoice:invoicemenu.html")
#     return render(request, "invoices/invoicesselllist.html", context)
