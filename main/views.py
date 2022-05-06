import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Team, Telephone, OrganisationTelephone, AccessModule, Command


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
    commands = Command.objects.all()
    date = datetime.date.today().today()
    context = {'date': date,
               'commands': commands}
    return render(request, 'main/welcome.html', context)


def give_access_to_modules(request):
    access = AccessModule.objects.all()

    context = {'access': access}
    return render(request, 'main/access_modules.html', context)
