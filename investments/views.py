from django.shortcuts import render


# Create your views here.
def investments_list(request):
    return render(request, 'investments/investments_main.html')


def investment_projects_list(request):
    return render(request, 'investments/investments_projects.html')
