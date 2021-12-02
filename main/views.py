from django.shortcuts import render


# Create your views here.
def telephone_list(request):
    context = {}
    return render(request, 'main/telephones.html', context)
