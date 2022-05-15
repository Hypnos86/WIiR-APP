from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from investments.models import Project


# Create your views here.
@login_required
def make_important_task_investments(request):
    return render(request, 'investments/investments_main.html')


@login_required()
def investment_projects_list(request):
    projects = Project.objects.all()
    projects_sum = len(projects)
    query = 'Wyczyść'
    search = 'Szukaj'

    paginator = Paginator(projects, 40)
    page_number = request.GET.get('page')
    projects_lis = paginator.get_page(page_number)

    q = request.GET.get('q')

    try:
        last_date = Project.objects.values('change').latest('change')
    except Project.DoesNotExist:
        last_date = None

    context = {'projects': projects,
               'query': query,
               'search': search,
               'last_date': last_date,
               'projects_sum': projects_sum
               }
    if q:
        projects = projects.filter(project_title__icontains=q) | projects.filter(
            unit__county__name__icontains=q) | projects.filter(unit__type__type_full__icontains=q) | projects.filter(
            unit__city__icontains=q) | projects.filter(section__section__startswith=q) | projects.filter(
            source_financing__icontains=q)
        return render(request, 'investments/investments_projects.html', {'projects': projects,
                                                                         'query': query,
                                                                         'last_date': last_date,
                                                                         'projects_sum': projects_sum})
    else:
        return render(request, 'investments/investments_projects.html', {'projects': projects_lis,
                                                                         'search': search,
                                                                         'last_date': last_date,
                                                                         'projects_sum': projects_sum})
