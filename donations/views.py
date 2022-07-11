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

    try:
        last_date = Application.objects.values('change').latest('change')
    except Application.DoesNotExist:
        last_date = None

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
    return render(request, 'donations/information_popup.html', {'donation': donation})
