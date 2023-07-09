from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View

from donations.models import Application
from donations.forms import ApplicationForm
from units.models import Unit
from main.views import now_date, current_year
from django.core.paginator import Paginator


# Create your views here.
class DonationsListView(LoginRequiredMixin, View):
    template = "donations/list_donations.html"

    def get(self, request, year):
        applications = Application.objects.all().filter(date_receipt__year=year).order_by('-date_receipt')
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
            context = {'application_len': application_len, 'query': query, 'year': year,
                       'applications': applications, 'last_date': last_date, 'q': q, 'date_from': date_from,
                       'date_to': date_to}
            return render(request, self.template, context)
        else:
            context = {'application_len': application_len, 'search': search, 'year': year,
                       'applications': application_paginator, 'last_date': last_date}
            return render(request, self.template, context)


class AddDonationView(LoginRequiredMixin, View):
    template = "donations/donation_form.html"

    form_class = ApplicationForm
    units = Unit.objects.all()

    def get(self, request, year):
        form = self.form_class

        context = {'new': True, 'donation_form': form, "units": self.units, "year": year}
        return render(request, self.template, context)

    def post(self, request, year):
        form = self.form_class(request.POST or None, request.FILES or None)

        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect(reverse('donations:donations_list', kwargs={"year": year}))
        context = {'new': True, 'donation_form': form, "units": self.units, "year": year}
        return render(request, self.template, context)


class EditDonationView(LoginRequiredMixin, View):
    template = "donations/donation_form.html"

    def get(self, request, year, slug):
        donation_edit = get_object_or_404(Application, slug=slug)
        donation_form = ApplicationForm(instance=donation_edit)
        units = Unit.objects.all()
        donation_unit = donation_edit.unit
        context = {'new': False, 'donation_form': donation_form, 'units': units, 'donation_unit': donation_unit,
                   "year": year, "id": donation_edit.id}
        return render(request, self.template, context)

    def post(self, request, year, slug):
        donation_edit = get_object_or_404(Application, slug=slug)
        donation_form = ApplicationForm(request.POST, request.FILES, instance=donation_edit)
        units = Unit.objects.all()
        donation_unit = donation_edit.unit

        if donation_form.is_valid():
            instance = donation_form.save(commit=False)
            instance.author = request.user
            donation_form.save()
            return redirect(reverse('donations:donations_list', kwargs={"year": year}))
        context = {'new': False, 'donation_form': donation_form, 'units': units, 'donation_unit': donation_unit,
                   "year": year, "id": donation_edit.id}
        return render(request, self.template, context)


class ShowInformationView(LoginRequiredMixin, View):
    template = "donations/donation_info_popup.html"

    def get(self, request, id):
        donation = get_object_or_404(Application, pk=id)
        context = {'donation': donation, 'id': id}
        return render(request, self.template, context)


class DonationsArchiveYearListView(LoginRequiredMixin, View):
    template = "donations/archive_list_year.html"

    def get(self, request):
        now_year = current_year()

        # Filtrowanie wniosków
        all_year_order = Application.objects.all().values('date_receipt__year').exclude(date_receipt__year=now_year)
        year_order_set = set([year['date_receipt__year'] for year in all_year_order])
        year_order_list = sorted(year_order_set, reverse=True)
        context = {'year_order_list': year_order_list}
        return render(request, self.template, context)


class DonationsArchiveListView(LoginRequiredMixin, View):
    template = "donations/list_donations.html"

    def get(self, request, year):
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
            context = {'application_len': application_len, 'query': query, 'year': year, 'applications': applications,
                       'last_date': last_date, 'archive': True, 'q': q, 'date_from': date_from, 'date_to': date_to,
                       "current_year": current_year()}
            return render(request, self.template, context)
        else:
            context = {'application_len': application_len, 'search': search, 'year': year,
                       'applications': application_paginator, 'last_date': last_date, 'archive': True,
                       "current_year": current_year()}
            return render(request, self.template, context)
