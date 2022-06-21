import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Team, Telephone, OrganisationTelephone, AccessModule, Command


def current_year():
    return datetime.date.today().year


def now_date():
    return datetime.datetime.now()


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
    commands = Command.objects.all().order_by('create_date')[:4]
    date = datetime.date.today().today()
    context = {'date': date,
               'commands': commands}
    return render(request, 'main/home.html', context)


@login_required
def give_access_to_modules(request):
    access = AccessModule.objects.all()
    commands = Command.objects.all()

    context = {'access': access,
               'commands': commands}
    return render(request, 'main/access_modules.html', context)


@login_required
def make_command_list(request):
    commands = Command.objects.all()
    return render(request, 'main/command.html', {'commands': commands})
