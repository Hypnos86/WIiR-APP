import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Team, Telephone, OrganisationTelephone


def current_year():
    return datetime.date.today().year


def year_choises():
    year = []
    for y in range(2000, datetime.date.today().year):
        year.append(y)
        year.sort(reverse=True)
    return year


# Create your views here.
@login_required
def telephone_list(request):
    teams = Team.objects.all()
    tel = Telephone.objects.all()
    telephone_book = OrganisationTelephone.objects.all()

    context = {'tel': tel,
               'teams': teams,
               'telephone_book': telephone_book}
    return render(request, 'main/telephones.html', context)


@login_required
def welcome(request):
    date = datetime.date.today().today()

    return render(request, 'main/welcome.html', {'date': date})
