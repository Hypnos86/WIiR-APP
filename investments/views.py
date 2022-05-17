from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from investments.models import Project
from investments.forms import ProjectForm
from units.models import Unit


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


@login_required
def add_new_project(request):
    project = ProjectForm(request.POST or None, request.FILES or None)
    units = Unit.objects.all()

    context = {'project_form': project,
               'units': units,
               'new': True
               }

    if request.method == 'POST':
        if project.is_valid():
            instance = project.save(commit=False)
            instance.author = request.user
            instance.save()
            project.save()
            return redirect('investments:investment_projects_list')
    return render(request, 'investments/project_form.html', context)


@login_required
def edit_project(request, id):
    project_edit = get_object_or_404(Project, pk=id)
    project_form = ProjectForm(request.POST or None, request.FILES or None, instance=project_edit)
    units = Unit.objects.all()

    context = {'project_form': project_form,
               'units': units,
               'new': False}

    if project_form.is_valid():
        instance = project_form.save(commit=False)
        instance.author = request.user
        instance.save()
        project_edit.save()
        return redirect('investments:investment_projects_list')
    return render(request, 'investments/project_form.html', context)


@login_required
def show_project(request, id):
    project = Project.objects.get(pk=id)
    context = {'project_form': project}

    return render(request, 'investments/show_project.html', context)
