from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import NeedsLetter, TeamType, RegistrationType
from .forms import NeedsLetterForm
from main.models import Employer
from units.models import Unit
from main.views import current_year


# Create your views here.

@login_required
def list_needs_letter(request, year):
    objects = NeedsLetter.objects.all().filter(receipt_date__year=year, isDone=False).order_by("-receipt_date")
    objectslen = len(objects)

    query = "Wyczyść"
    search = "Szukaj"
    q = request.GET.get("q")

    paginator = Paginator(objects, 50)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)

    try:
        last_date = NeedsLetter.objects.values('change').latest('change')
    except NeedsLetter.DoesNotExist:
        last_date = None

    if q:
        objects = objects.filter(case_sign__icontains=q) \
                  | objects.filter(unit__county__name__icontains=q) \
                  | objects.filter(unit__city__icontains=q) \
                  | objects.filter(case_type__metric_type__icontains=q) \
                  | objects.filter(registration_type__registration_type__icontains=q) \
                  | objects.filter(employer__name__icontains=q) \
                  | objects.filter(employer__last_name__icontains=q) \
                  | objects.filter(no_secretariats_diary__icontains=q)

        return render(request, 'operationalneedsrecords/needs_letter_list.html',
                      {"objects": objects, "last_date": last_date, "objectslen": objectslen,
                       "year": year, "q": q, 'query': query, "archive": False})

    else:
        return render(request, 'operationalneedsrecords/needs_letter_list.html',
                      {"objects": objects_list, "last_date": last_date, "objectslen": objectslen, 'search': search,
                       "year": year, "q": q, "archive": False})


@login_required
def list_needs_letter_archive(request, year):
    objects = NeedsLetter.objects.all().filter(receipt_date__year=year, isDone=True).order_by("-receipt_date")
    objectslen = len(objects)

    try:
        last_date = NeedsLetter.objects.values('change').latest('change')
    except NeedsLetter.DoesNotExist:
        last_date = None

    paginator = Paginator(objects, 50)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)

    return render(request, 'operationalneedsrecords/needs_letter_list.html',
                  {"objects": objects_list, "last_date": last_date, "objectslen": objectslen, "search": True,
                   "year": year, "archive": True})


@login_required
def new_needs_latter(request, year):
    object_form = NeedsLetterForm(request.POST or None)
    object_form.fields['employer'].queryset = Employer.objects.all().filter(team=TeamType.ZE.value)
    units = Unit.objects.all()

    if request.method == 'POST':
        if object_form.is_valid():
            instance = object_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(reverse('operationalneedsrecords:list_needs_letter', kwargs={"year": year}))
    return render(request, 'operationalneedsrecords/needs_letter_form.html',
                  {"object_form": object_form, "units": units, "new": True, "year": year})


@login_required
def edit_needs_letter(request, year, id):
    object_letter = get_object_or_404(NeedsLetter, pk=id)
    object_form = NeedsLetterForm(request.POST or None, instance=object_letter)
    object_form.fields['employer'].queryset = Employer.objects.all().filter(team=TeamType.ZE.value)
    units = Unit.objects.all()
    object_edit = object_letter.unit

    if request.method == "POST":
        if object_form.is_valid():
            instance = object_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(reverse('operationalneedsrecords:list_needs_letter', kwargs={"year": year}))
    return render(request, 'operationalneedsrecords/needs_letter_form.html',
                  {"object_form": object_form, "units": units, "object_edit": object_edit, "new": False, "year": year,
                   "id": id})


@login_required
def needs_letter_show(request, year, id):
    object = get_object_or_404(NeedsLetter, pk=id)
    return render(request, 'operationalneedsrecords/needs_letter_show.html', {"object": object, "year": year})


@login_required
def show_archive_year_list(request):
    now_year = current_year()
    # Filtrowanie pism

    all_year_order = NeedsLetter.objects.all().values('receipt_date__year').exclude(receipt_date__year=now_year)
    year_order_set = set([year['receipt_date__year'] for year in all_year_order])
    year_order_list = sorted(year_order_set, reverse=True)

    return render(request, 'operationalneedsrecords/archive_list_year.html', {'year_order_list': year_order_list})


@login_required
def show_statistic(request, year):
    documents = NeedsLetter.objects.all().filter(receipt_date__year=year)
    registrationTypes = RegistrationType.objects.all()

    counts = []
    employers_set = set()
    for doc in documents:
        counts.append(doc.cost)
        doc.employer
        employers_set.add(doc.employer)

    count_all = sum(counts)
    print(employers_set)
    registrationTypeList = []

    for registrationType in registrationTypes:
        docsObjects = documents.filter(registration_type__id=registrationType.id)
        sum_type = 0
        countType = []
        for docsobject in docsObjects:
            sum_type += docsobject.cost
            countType.append(sum_type)
        newObjectType = {"type": registrationType, "sumType": sum_type, 'countType': countType}
        registrationTypeList.append(newObjectType)

    return render(request, 'operationalneedsrecords/statistics.html',
                  {'year': year, 'docs': documents, "count_all": count_all, "registrationTypes": registrationTypes,
                   "registrationTypeList": registrationTypeList})
