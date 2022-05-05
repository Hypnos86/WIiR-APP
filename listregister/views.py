from django.shortcuts import render


# Create your views here.
def make_list_register(request):
    return render(request, 'list_register.html')
