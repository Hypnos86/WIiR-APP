import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Team, Telephone, OrganisationTelephone, AccessModule, Command, Employer
from businessflats.models import OfficialFlat
from contracts.models import ContractImmovables, ContractAuction
from contractors.models import Contractor
from donations.models import Application
from gallery.models import Gallery
from investments.models import Project
from cpvdict.models import Genre


def current_year():
    return datetime.date.today().year


def now_date():
    return datetime.datetime.now()


# Create your views here.
@login_required
def welcome(request):
    commands = Command.objects.all().order_by('create_date')[:4]
    date = datetime.date.today().today()
    context = {'date': date,
               'commands': commands}
    return render(request, 'main/home.html', context)


@login_required
def make_secretariat_site(request):
    return render(request, 'main/secretariat_menu.html')


@login_required
def show_teams_list(request):
    teams = Team.objects.all()
    return render(request, 'main/teams_list.html', {'teams': teams})


@login_required
def show_employers_list(request):
    employers = Employer.objects.all()
    return render(request, 'main/employers_list.html', {'employers': employers})


@login_required
def show_command_list(request):
    commands = Command.objects.all()
    return render(request, 'main/commands_list.html', {'commands': commands})


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
def give_access_to_modules(request):
    access = AccessModule.objects.all()
    commands = Command.objects.all()

    context = {'access': access,
               'commands': commands}
    return render(request, 'main/access_modules.html', context)


@login_required
def show_command(request):
    commands = Command.objects.all()
    return render(request, 'main/command.html', {'commands': commands})


@login_required
def make_list_register(request):
    contracts = ContractImmovables.objects.all().filter(state=True)
    contract_len = len(contracts)

    flats = OfficialFlat.objects.all()
    count_flats = len(flats)

    contractors = Contractor.objects.all()
    contractors_len = len(contractors)

    application = Application.objects.all().filter(date_receipt__year=current_year())
    application_len = len(application)

    contracts_auction = ContractAuction.objects.all()
    contracts_auction_len = len(contracts_auction)

    galleries = Gallery.objects.all()
    galleries_len = len(galleries)

    projects = Project.objects.all()
    projects_len = len(projects)

    genres = Genre.objects.all().exclude(name_id='RB')
    genres_len = len(genres)

    context = {'count_flats': count_flats, 'con_len': contract_len, 'contractors_len': contractors_len,
               'application_len': application_len, 'contracts_auction_len': contracts_auction_len,
               'galleries_len': galleries_len, 'projects_len': projects_len, 'genres_len': genres_len}
    return render(request, 'main/list_register.html', context)
