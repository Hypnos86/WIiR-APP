from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from donations.models import Application
from donations.forms import ApplicationForm
from units.models import Unit
from main.views import now_date, current_year
from django.core.paginator import Paginator


# Create your views here.

@login_required
def donations_list(request):
    applications = Application.objects.all().filter(date_receipt__year=current_year()).order_by('-date_receipt')
    query = "Wyczyść"
    search = "Szukaj"
    application_len = len(applications)
    year = current_year()
    q = request.GET.get("q")

    paginator = Paginator(applications, 40)
    page_number = request.GET.get('page')
    application_paginator = paginator.get_page(page_number)
    date_from = request.GET.get('from', None)
    date_to = request.GET.get('to', None)

    try:
        last_date = Application.objects.values('change').latest('change')
    except Application.DoesNotExist:
        last_date = None

    if q or date_from or date_to:
        if q:
            applications = applications.filter(character__icontains=q) \
                           | applications.filter(no_application__icontains=q) \
                           | applications.filter(donation_type__type_name__icontains=q) \
                           | applications.filter(financial_type__type_name__icontains=q) \
                           | applications.filter(sum__startswith=q) \
                           | applications.filter(unit__county__name__icontains=q) \
                           | applications.filter(unit__city__icontains=q) \
                           | applications.filter(presenter__name__icontains=q)

        if date_from:
            applications = applications.filter(date_receipt__gte=date_from)
        if date_to:
            applications = applications.filter(date_receipt__lte=date_to)

        return render(request, 'donations/donations_list.html',
                      {'application_len': application_len, 'query': query, 'year': year,
                       'applications': applications, 'last_date': last_date, 'q': q, 'date_from': date_from,
                       'date_to': date_to})
    else:
        return render(request, 'donations/donations_list.html',
                      {'application_len': application_len, 'search': search, 'year': year,
                       'applications': application_paginator, 'last_date': last_date})


@login_required
def add_donation(request):
    donation_form = ApplicationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if donation_form.is_valid():
            instance = donation_form.save(commit=False)
            instance.author = request.user
            donation_form.save()
            return redirect('donations:donations_list')
    return render(request, 'donations/donation_form.html', {'new': True, 'donation_form': donation_form})


@login_required
def edit_donation(request, id):
    donation_edit = get_object_or_404(Application, pk=id)
    donation_form = ApplicationForm(request.POST or None, request.FILES or None, instance=donation_edit)
    units = Unit.objects.all()
    donation_edit = donation_edit.unit
    if request.method == 'POST':
        if donation_form:
            instance = donation_form.save(commit=False)
            instance.author = request.user
            donation_form.save()
            return redirect('donations:donations_list')
    return render(request, 'donations/donation_form.html',
                  {'new': False, 'donation_form': donation_form, 'units': units, 'donation_edit': donation_edit})


@login_required
def show_information_popup(request, id):
    donation = get_object_or_404(Application, pk=id)
    return render(request, 'donations/info_donation_popup.html', {'donation': donation, 'id': id})


@login_required
def show_archive_year_list(request):
    now_year = current_year()
    # Filtrowanie wniosków
    all_year_order = Application.objects.all().values('date_receipt__year').exclude(date_receipt__year=now_year)
    year_order_set = set([year['date_receipt__year'] for year in all_year_order])
    year_order_list = sorted(year_order_set, reverse=True)

    return render(request, 'donations/archive_list_year.html', {'year_order_list': year_order_list})

@login_required
def donations_list_archive(request, year):
    applications = Application.objects.all().filter(date_receipt__year=year).order_by('-date_receipt')
    query = "Wyczyść"
    search = "Szukaj"
    application_len = len(applications)
    year = year
    q = request.GET.get("q")

    paginator = Paginator(applications, 40)
    page_number = request.GET.get('page')
    application_paginator = paginator.get_page(page_number)
    date_from = request.GET.get('from', None)
    date_to = request.GET.get('to', None)

    try:
        last_date = Application.objects.values('change').latest('change')
    except Application.DoesNotExist:
        last_date = None

    if q or date_from or date_to:
        if q:
            applications = applications.filter(character__icontains=q) \
                           | applications.filter(no_application__icontains=q) \
                           | applications.filter(donation_type__type_name__icontains=q) \
                           | applications.filter(financial_type__type_name__icontains=q) \
                           | applications.filter(sum__startswith=q) \
                           | applications.filter(unit__county__name__icontains=q) \
                           | applications.filter(unit__city__icontains=q) \
                           | applications.filter(presenter__name__icontains=q)

        if date_from:
            applications = applications.filter(date_receipt__gte=date_from)
        if date_to:
            applications = applications.filter(date_receipt__lte=date_to)

        return render(request, 'donations/donations_list.html',
                      {'application_len': application_len, 'query': query, 'year': year,
                       'applications': applications, 'last_date': last_date, 'q': q, 'date_from': date_from,
                       'date_to': date_to})
    else:
        return render(request, 'donations/donations_list.html',
                      {'application_len': application_len, 'search': search, 'year': year,
                       'applications': application_paginator, 'last_date': last_date, 'archive':True})