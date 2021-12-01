from django.shortcuts import render


# Create your views here.
def menu_invoices(request):
    return render(request, 'invoices/invoicesmenu.html')
