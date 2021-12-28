from django.shortcuts import render


# Create your views here.
def investments_list(request):
    return render(request, 'investments/investmentslist.html')
