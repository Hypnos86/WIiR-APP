from django.shortcuts import render
from donations.models import Application
from main.views import now_date, current_year
from django.core.paginator import Paginator


# Create your views here.
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
