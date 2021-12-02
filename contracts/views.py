from django.shortcuts import render


# Create your views here.
def menu_contracts(request):
    return render(request, 'contracts/contractlist.html')


def new_contracts(request):
    return render(request, 'contracts/newcontract.html')
