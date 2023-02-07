from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from main.models import Team, OrganisationTelephone, AccessModule, Command, Employer, SecretariatTelephone, Car
from main.forms import TeamForm, EmployerForm, CommandsForm, SecretariatTelephoneForm, CarForm
from businessflats.models import OfficialFlat
from units.models import Unit
from contracts.models import ContractImmovables, ContractAuction, ContractMedia
from contractors.models import Contractor
from donations.models import Application
from gallery.models import Gallery
from investments.models import Project
from cpvdict.models import Genre
from invoices.models import InvoiceBuy, InvoiceSell, CorrectiveNote
from fixedasset.models import Building
from operationalneedsrecords.models import NeedsLetter


def current_year():
    return datetime.date.today().year


def now_date():
    return datetime.datetime.now()


# Create your views here.
@login_required()
def welcome(request):
    commands = Command.objects.all().order_by("create_date")[:6]
    rent_cars = Car.objects.all()[:10]
    date = datetime.date.today().today()
    context = {"date": date,
               "commands": commands,
               "rent_cars": rent_cars}
    return render(request, "main/home.html", context)


@login_required
def add_rent_car(request):
    rent_car = CarForm(request.POST or None)
    context = {'rent_car': rent_car, 'new': True}
    if request.method == "POST":
        if rent_car.is_valid():
            instance = rent_car.save(commit=False)
            instance.author = request.user
            rent_car.save()
            return redirect('main:welcome')
    return render(request, 'main/car_popup.html', context)


@login_required
def edit_rent_car(request, id):
    car = get_object_or_404(Car, pk=id)
    rent_car_form = CarForm(request.POST or None, instance=car)

    if request.method == "POST":
        if rent_car_form.is_valid():
            instance = rent_car_form.save(commit=False)
            instance.author = request.user
            rent_car_form.save()
            return redirect("main:welcome")
    return render(request, 'main/car_popup.html', {'rent_car': rent_car_form, 'id': id, 'new': False})


@login_required
def delete_rent_car(request, id):
    rent_car = get_object_or_404(Car, pk=id)
    rent_car.delete()
    return redirect("main:welcome")


@login_required
def make_secretariat_site(request):
    return render(request, "main/secretariat_menu.html")


@login_required
def show_teams_list(request):
    teams = Team.objects.all().filter(active=True).order_by("priority")
    return render(request, "main/teams_list.html", {"teams": teams})


def add_team_popup(request):
    team_form = TeamForm(request.POST or None)
    team_form.fields["team"].label = "Nowa komórka Wydziału"

    if request.method == "POST":
        if team_form.is_valid():
            instance = team_form.save(commit=False)
            instance.active = True
            team_form.save()
            return redirect("main:show_teams_list")
    return render(request, "main/team_form_popup.html", {"team_form": team_form, "new": True})


def edit_team_popup(request, id):
    team = get_object_or_404(Team, pk=id)
    team_form = TeamForm(request.POST or None, instance=team)

    if request.method == "POST":
        if team_form.is_valid():
            team_form.save()
            return redirect("main:show_teams_list")
    return render(request, "main/team_form_popup.html", {"team_form": team_form, "new": False, "id": id})


@login_required
def show_employers_list(request):
    employers = Employer.objects.all().filter(deleted=False).order_by("team__priority")
    try:
        last_date = Employer.objects.values("change").latest("change")
    except Employer.DoesNotExist:
        last_date = None

    secretariat = SecretariatTelephone.objects.last()
    context = {"employers": employers, "last_date": last_date, "secretariat": secretariat}
    return render(request, "main/employers_list.html", context)


@login_required
def add_employer_popup(request):
    employer_form = EmployerForm(request.POST or None)

    if request.method == "POST":
        if employer_form.is_valid():
            instance = employer_form.save(commit=False)
            instance.author = request.user
            employer_form.save()
            return redirect("main:show_employers_list")
    return render(request, "main/employer_form_popup.html", {"employer_form": employer_form, "new": True})


@login_required
def edit_employer_popup(request, id):
    employer = get_object_or_404(Employer, pk=id)
    employer_form = EmployerForm(request.POST or None, instance=employer)
    employer_form.fields["deleted"].label = "Usuń pracownika"

    if request.method == "POST":
        if employer_form.is_valid():
            instance = employer_form.save(commit=False)
            instance.author = request.user
            employer_form.save()
            return redirect("main:show_employers_list")
    return render(request, "main/employer_form_popup.html", {"employer_form": employer_form, "id": id, "new": False})


@login_required
def show_command_list(request):
    commands = Command.objects.all().order_by("-create_date")
    commands_len = len(commands)
    try:
        last_date = Command.objects.values("change").latest("change")
    except Command.DoesNotExist:
        last_date = None
    return render(request, "main/command.html",
                  {"commands": commands, "last_date": last_date, "commands_len": commands_len, "secretariat": True})


@login_required
def add_command_popup(request):
    command_form = CommandsForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if command_form.is_valid():
            command_form.save()
            return redirect("main:show_command_list")
    return render(request, "main/command_form_popup.html", {"command_form": command_form, "new": True})


@login_required
def edit_command_popup(request, id):
    command_edit = get_object_or_404(Command, pk=id)
    command_form = CommandsForm(request.POST or None, request.FILES or None, instance=command_edit)
    if request.method == "POST":
        if command_form.is_valid():
            command_form.save()
            return redirect("main:show_command_list")
    return render(request, "main/command_form_popup.html", {"command_form": command_form, "id": id, "new": False})


@login_required
def delete_command_popup(request, id):
    command = get_object_or_404(Command, pk=id)
    command.delete()
    return redirect("main:show_command_list")


@login_required
def telephone_list(request):
    teams = Team.objects.all().filter(active=True).order_by("priority")
    telephone_book = OrganisationTelephone.objects.all()
    secretariat = SecretariatTelephone.objects.last()
    context = {"teams": teams, "telephone_book": telephone_book, "secretariat": secretariat}
    return render(request, "main/telephones.html", context)


@login_required
def add_secretariat_number(request):
    secretariat_form = SecretariatTelephoneForm(request.POST or None)
    if request.method == "POST":
        if secretariat_form.is_valid():
            secretariat_form.save()
            return redirect("main:show_employers_list")
    return render(request, "main/secretariat_form_popup.html", {"secretariat_form": secretariat_form, "new": True})


@login_required
def edit_secretariat_number(request, id):
    secretariat_edit = get_object_or_404(SecretariatTelephone, pk=id)
    secretariat_form = SecretariatTelephoneForm(request.POST or None, instance=secretariat_edit)
    if request.method == "POST":
        if secretariat_form.is_valid():
            secretariat_form.save()
            return redirect("main:show_employers_list")
    return render(request, "main/secretariat_form_popup.html",
                  {"secretariat_form": secretariat_form, "new": False, "id": id})


@login_required
def delete_secretariat_number(request, id):
    instance = get_object_or_404(SecretariatTelephone, pk=id)
    instance.delete()
    return redirect("main:show_employers_list")


@login_required
def give_access_to_modules(request):
    access = AccessModule.objects.all()
    commands = Command.objects.all()
    context = {"access": access, "commands": commands}
    return render(request, "main/access_modules.html", context)


@login_required
def make_list_register(request):
    now_year = current_year()
    # Zespół Nieruchomości
    contracts = ContractImmovables.objects.all().filter(state=True)
    contract_len = len(contracts)

    units_len = len(Unit.objects.all().filter(status=True))

    # Zespół Mieszkaniowy
    flats = OfficialFlat.objects.all()
    count_flats = len(flats)

    # Zespół Rozliczeń i Wsparcia technicznego
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

    genres = Genre.objects.all().exclude(name_id="RB")
    genres_len = len(genres)

    invoices_sell = InvoiceSell.objects.all().filter(date__year=current_year())
    invoices_sell_len = len(invoices_sell)

    invoices_buy = InvoiceBuy.objects.all().filter(date_receipt__year=current_year())
    invoices_buy_len = len(invoices_buy)

    corrective_note = CorrectiveNote.objects.all().filter(date__year=current_year())
    corrective_note_len = len(corrective_note)

    contracts_media = ContractMedia.objects.all().filter(state=True)
    contracts_media_len = len(contracts_media)

    buildings = Building.objects.all().filter(state=True)
    buildings_len = len(buildings)

    # Zespoł Eksploatacji

    letters = NeedsLetter.objects.all().filter(receipt_date__year=current_year())
    letters_len = len(letters)

    context = {"units_len": units_len, "count_flats": count_flats, "con_len": contract_len,
               "contractors_len": contractors_len, "application_len": application_len,
               "contracts_auction_len": contracts_auction_len, "galleries_len": galleries_len,
               "projects_len": projects_len, "genres_len": genres_len, "invoices_sell_len": invoices_sell_len,
               "invoices_buy_len": invoices_buy_len, "corrective_note_len": corrective_note_len,
               "contracts_media_len": contracts_media_len, "buildings_len": buildings_len, "letters_len": letters_len,
               "now_year": now_year}
    return render(request, "main/list_register.html", context)
