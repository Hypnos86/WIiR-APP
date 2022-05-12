from django.shortcuts import render
from investments.models import Project


# Create your views here.
def investments_list(request):
    return render(request, 'investments/investments_main.html')


def investment_projects_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'investments/investments_projects.html', context)
