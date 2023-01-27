from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import NeedsLetter, TeamType
from .forms import NeedsLetterForm
from main.models import Employer
from units.models import Unit
from main.views import current_year


# Create your views here.

@login_required
def list_needs_letter(request):
    year = current_year()
    objects = NeedsLetter.objects.all().filter(receipt_date__year=year, isDone=False).order_by("-receipt_date")
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
                   "year": year})


@login_required
def new_needs_latter(request):
    object_form = NeedsLetterForm(request.POST or None)
    object_form.fields['employer'].queryset = Employer.objects.all().filter(team=TeamType.ZE.value)
    units = Unit.objects.all()

    if request.method == 'POST':
        if object_form.is_valid():
            instance = object_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('operationalneedsrecords:list_needs_letter')
    return render(request, 'operationalneedsrecords/needs_letter_form.html',
                  {"object_form": object_form, "units": units, "new": True})


@login_required
def edit_needs_letter(request, id):
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
            return redirect('operationalneedsrecords:list_needs_letter')
    return render(request, 'operationalneedsrecords/needs_letter_form.html',
                  {"object_form": object_form, "units": units, "object_edit":object_edit, "new": False})
