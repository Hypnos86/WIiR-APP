from django.shortcuts import render


# Create your views here.
def menu_invoices(request):
    return render(request, 'invoices/invoicesmenu.html')


def buy_invoices(request):
    return render(request, 'invoices/invoicesbuy.html')


def sell_invoices(request):
    return render(request, 'invoices/invoicessell.html')
