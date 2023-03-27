from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
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


class WelcomeView(LoginRequiredMixin, View):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        commands = Command.objects.all().order_by("create_date")[:6]
        rent_cars = Car.objects.all()[:10]
        date = datetime.date.today().today()
        context = {"date": date,
                   "commands": commands,
                   "rent_cars": rent_cars}
        return render(request, self.template_name, context)


class NewRentCatView(LoginRequiredMixin, View):
    template_name = 'main/car_form.html'
    form_class = CarForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'rent_car': form, 'new': True}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            return redirect('main:welcome')
        context = {'rent_car': form, 'new': True}
        return render(request, self.template_name, context)


class EditRentCarView(LoginRequiredMixin, View):
    template_name = 'main/car_form.html'
    form_class = CarForm

    def get(self, request, id, *args, **kwargs):
        car = get_object_or_404(Car, pk=id)
        form = self.form_class(instance=car)
        context = {'rent_car': form, 'id': id, 'new': False}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        car = get_object_or_404(Car, pk=id)
        form = self.form_class(request.POST or None, instance=car)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            return redirect("main:welcome")
        context = {'rent_car': form, 'id': id, 'new': False}
        return render(request, self.template_name, context)


class DeleteRentCar(LoginRequiredMixin, View):
    def get(self, request, id):
        rent_car = get_object_or_404(Car, pk=id)
        rent_car.delete()
        return redirect('main:welcome')


class SecretariatSiteView(LoginRequiredMixin, View):
    template_name = 'main/secretariat_menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ShowTeamsListView(LoginRequiredMixin, View):
    template_name = 'main/teams_list.html'

    def get(self, request, *args, **kwargs):
        teams = Team.objects.all().filter(active=True).order_by("priority")
        context = {'teams': teams}
        return render(request, self.template_name, context)


class NewTeamView(LoginRequiredMixin, View):
    template_name = 'main/team_form_popup.html'
    form_class = TeamForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'team_form': form, 'new': True}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.active = True
            form.save()
            return redirect('main:show_teams_list')
        context = {'team_form': form, 'new': True}
        return render(request, self.template_name, context)


class EditTeamView(LoginRequiredMixin, View):
    template_name = 'main/team_form_popup.html'
    form_class = TeamForm

    def get(self, request, id, *args, **kwargs):
        team = get_object_or_404(Team, pk=id)
        form = self.form_class(instance=team)
        context = {'team_form': form, 'new': False, 'id': id}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        team = get_object_or_404(Team, pk=id)
        form = self.form_class(request.POST or None, instance=team)
        if form.is_valid():
            form.save()
            return redirect('main:show_teams_list')
        context = {'team_form': form, 'new': False, 'id': id}
        return render(request, self.template_name, context)


class EmployersListView(LoginRequiredMixin, View):
    template_name = 'main/employers_list.html'

    def get(self, request, *args, **kwargs):
        employers = Employer.objects.all().filter(deleted=False).order_by("team__priority")
        try:
            last_date = Employer.objects.values("change").latest("change")
        except Employer.DoesNotExist:
            last_date = None

        secretariat = SecretariatTelephone.objects.last()
        context = {"employers": employers, "last_date": last_date, "secretariat": secretariat}
        return render(request, self.template_name, context)


class NewEmployerView(LoginRequiredMixin, View):
    teamplate_name = 'main/employer_form_popup.html'
    form_class = EmployerForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'employer_form': form, 'new': True}
        return render(request, self.teamplate_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            return redirect('main:show_employers_list')
        context = {'employer_form': form, 'new': True}
        return render(request, self.teamplate_name, context)


class EditEmployerView(LoginRequiredMixin, View):
    template_name = 'main/employer_form_popup.html'
    form_class = EmployerForm

    def get(self, request, id, *args, **kwargs):
        employer = get_object_or_404(Employer, pk=id)
        form = self.form_class(instance=employer)
        context = {'employer_form': form, 'id': id, 'new': False}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        employer = get_object_or_404(Employer, pk=id)
        form = self.form_class(request.POST or None, instance=employer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            return redirect('main:show_employers_list')
        context = {'employer_form': form, 'id': id, 'new': False}
        return render(request, self.template_name, context)


class CommandListView(LoginRequiredMixin, View):
    template_name = 'main/command.html'

    def get(self, request, *args, **kwargs):
        commands = Command.objects.all().order_by("-create_date")
        commands_len = len(commands)
        try:
            last_date = Command.objects.values("change").latest("change")
        except Command.DoesNotExist:
            last_date = None
        context = {'commands': commands, 'last_date': last_date, 'commands_len': commands_len, 'secretariat': True}
        return render(request, self.template_name, context)


class AddCommandView(LoginRequiredMixin, View):
    template_name = 'main/command_form_popup.html'
    form_class = CommandsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('main:show_command_list')
        context = {'command_form': form, 'new': True}
        return render(request, self.template_name, context)


class EditCommandView(LoginRequiredMixin, View):
    template_name = 'main/command_form_popup.html'
    form_class = CommandsForm

    def get(self, request, id, *args, **kwargs):
        command = get_object_or_404(Command, pk=id)
        form = self.form_class(instance=command)
        context = {'command_form': form, 'id': id, 'new': False}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        command = get_object_or_404(Command, pk=id)
        form = self.form_class(request.POST or None, instance=command)
        if form.is_valid():
            form.save()
            return redirect('main:show_command_list')
        context = {'command_form': form, 'id': id, 'new': False}
        return render(request, self.template_name, context)


class DeleteCommandView(LoginRequiredMixin, View):
    def get(self, request, id):
        command = get_object_or_404(Command, pk=id)
        command.delete()
        return redirect("main:show_command_list")


class TelephoneListView(LoginRequiredMixin, View):
    template_name = 'main/telephones.html'

    def get(self, request, *args, **kwargs):
        teams = Team.objects.all().filter(active=True).order_by("priority")
        telephone_book = OrganisationTelephone.objects.all()
        secretariat = SecretariatTelephone.objects.last()
        context = {"teams": teams, "telephone_book": telephone_book, "secretariat": secretariat}
        return render(request, self.template_name, context)


class NewSecretariatNumberView(LoginRequiredMixin, View):
    template_name = 'main/secretariat_form_popup.html'
    form_class = SecretariatTelephoneForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'secretariat_form': form, 'new': True}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('main:show_employers_list')
        context = {'secretariat_form': form, 'new': True}
        return render(request, self.template_name, context)


class EditSecretariatNumberView(LoginRequiredMixin, View):
    template_name = 'main/secretariat_form_popup.html'
    form_class = SecretariatTelephoneForm

    def get(self, request, id, *args, **kwargs):
        instance = get_object_or_404(SecretariatTelephone, pk=id)
        form = self.form_class(instance=instance)
        context = {'secretariat_form': form, 'new': False, 'id': id}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        instance = get_object_or_404(SecretariatTelephone, pk=id)
        form = self.form_class(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main:show_employers_list')
        context = {'secretariat_form': form, 'new': False, 'id': id}
        return render(request, self.template_name, context)


class DeleteSecretariatNumberView(LoginRequiredMixin, View):

    def get(self, request, id):
        instance = get_object_or_404(SecretariatTelephone, pk=id)
        instance.delete()
        return redirect('main:show_employers_list')


class AccessToModulesView(LoginRequiredMixin, View):
    template_name = 'main/access_modules.html'

    def get(self, request, *args, **kwargs):
        access = AccessModule.objects.all()
        commands = Command.objects.all()
        context = {"access": access, "commands": commands}
        return render(request, self.template_name, context)


class ListRegisterView(LoginRequiredMixin, View):
    template_name = 'main/list_register.html'
    now_year = current_year()

    def get(self, request, *args, **kwargs):
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
                   "contracts_media_len": contracts_media_len, "buildings_len": buildings_len,
                   "letters_len": letters_len,
                   "now_year": self.now_year}
        return render(request, self.template_name, context)
