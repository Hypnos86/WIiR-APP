from django.shortcuts import render


# Create your views here.
def menu_contractsimmovables(request):
    context = {}
    return render(request, 'contracts/contractlist.html', context)


def new_contractsimmovables(request):
    context = {}
    return render(request, 'contracts/newcontract.html', context)


def edit_contractsimmovables(request):
    context = {}
    return render(request, 'contracts/editcontract.html', context)
