from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from investments.models import Project
from investments.forms import ProjectForm
from units.models import Unit
from contracts.models import ContractAuction, SettlementContractAuction
from contracts.forms import ContractAuctionForm
from main.models import Employer
from gallery.models import Gallery


# Create your views here.
@login_required
def make_important_task_investments(request):
    settelments = SettlementContractAuction.objects.all()
    return render(request, 'investments/investments_main.html', {'settelments': settelments})


@login_required()
def investment_projects_list(request):
    projects = Project.objects.all().order_by('-date_of_acceptance')
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

    if q:
        projects = projects.filter(project_title__icontains=q) \
                   | projects.filter(unit__county__name__icontains=q) \
                   | projects.filter(unit__type__type_full__icontains=q) \
                   | projects.filter(unit__city__icontains=q) \
                   | projects.filter(section__section__startswith=q) \
                   | projects.filter(source_financing__icontains=q) \
                   | projects.filter(date_of_acceptance__year=q)
        return render(request, 'investments/investments_projects.html', {'projects': projects,
                                                                         'query': query,
                                                                         'last_date': last_date,
                                                                         'projects_sum': projects_sum, 'q': q})
    else:
        return render(request, 'investments/investments_projects.html', {'projects': projects_lis,
                                                                         'search': search,
                                                                         'last_date': last_date,
                                                                         'projects_sum': projects_sum})


@login_required
def add_new_project(request):
    project_form = ProjectForm(request.POST or None, request.FILES or None)
    project_form.fields['worker'].queryset = Employer.objects.filter(industry_specialist=True)
    units = Unit.objects.all()

    context = {'project_form': project_form,
               'units': units,
               'new': True
               }

    if request.method == 'POST':
        if project_form.is_valid():
            instance = project_form.save(commit=False)
            instance.author = request.user
            project_form.save()
            return redirect('investments:investment_projects_list')
    return render(request, 'investments/project_form.html', context)


@login_required
def edit_project(request, id):
    project_edit = get_object_or_404(Project, pk=id)
    project_form = ProjectForm(request.POST or None, request.FILES or None, instance=project_edit)
    project_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all()
    unit_edit = project_edit.unit

    context = {'project_form': project_form,
               'units': units,
               'project': project_edit,
               'unit_edit': unit_edit,
               'new': False}

    if request.method == 'POST':
        if project_form.is_valid():
            instance = project_form.save(commit=False)
            instance.author = request.user
            project_form.save()
            return redirect('investments:investment_projects_list')
    return render(request, 'investments/project_form.html', context)


@login_required
def show_project(request, id):
    project = Project.objects.get(pk=id)
    galleries = project.gallery.all()
    contracts = project.contract_auction.all()
    context = {'project_form': project,
               'contracts': contracts,
               'galleries': galleries
               }
    return render(request, 'investments/show_project.html', context)


@login_required
def show_galleries_popup(request, id):
    project = Project.objects.get(pk=id)
    galleries = project.gallery.all()
    context = {'id': id,
               'galleries': galleries}
    return render(request, "investments/show_galleries_popup.html", context)


@login_required
def add_contract_to_project(request, id):
    project = get_object_or_404(Project, pk=id)
    contracts = ContractAuction.objects.all().filter(investments_project=None)

    if request.method == 'POST':
        selected_contract = request.POST.get('choice')
        if selected_contract:
            contract = get_object_or_404(ContractAuction, pk=selected_contract)
            contract.investments_project = project
            contract.save()
        return redirect(reverse('investments:edit_project', kwargs={'id': id}))

    return render(request, 'investments/add_contract_to_project_form.html', {'contracts': contracts,
                                                                             'project_id': id})
