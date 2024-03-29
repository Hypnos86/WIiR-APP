import logging
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Team, OrganisationTelephone, AccessModule, Command, Employer, SecretariatTelephone, Car, \
    NecesseryFile
from main.forms import TeamForm, EmployerForm, CommandForm, SecretariatTelephoneForm, CarForm, NecesseryFileForm
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

logger = logging.getLogger(__name__)


def current_year():
    return datetime.date.today().year


def now_date():
    return datetime.datetime.now()


class WelcomeView(LoginRequiredMixin, View):
    template = 'main/home.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            commands = Command.objects.all().order_by("create_date")[:6]
            rent_cars = Car.objects.all()[:10]
            date = datetime.date.today().today()
            context = {"date": date,
                       "commands": commands,
                       "rent_cars": rent_cars}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewRentCatView(LoginRequiredMixin, View):
    template = 'main/car_form.html'
    template_error = 'main/error_site.html'
    form_class = CarForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'rent_car': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect('main:welcome')
            context = {'rent_car': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditRentCarView(LoginRequiredMixin, View):
    template = 'main/car_form.html'
    template_error = 'main/error_site.html'
    form_class = CarForm

    def get(self, request, id):
        try:
            car = get_object_or_404(Car, pk=id)
            form = self.form_class(instance=car)
            context = {'rent_car': form, 'id': id, 'new': False}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            car = get_object_or_404(Car, pk=id)
            form = self.form_class(request.POST or None, instance=car)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect("main:welcome")
            context = {'rent_car': form, 'id': id, 'new': False}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DeleteRentCar(LoginRequiredMixin, View):
    def get(self, request, id):
        try:
            rent_car = get_object_or_404(Car, pk=id)
            rent_car.delete()
            return redirect('main:welcome')
        except Exception as e:
            logger.error("Error: %s", e)


class SecretariatSiteView(LoginRequiredMixin, View):
    template = 'main/secretariat_menu.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            return render(request, self.template)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowTeamsListView(LoginRequiredMixin, View):
    template = 'main/teams_list.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            teams = Team.objects.all().filter(active=True).order_by("priority")
            context = {'teams': teams}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewTeamView(LoginRequiredMixin, View):
    template = 'main/team_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = TeamForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'team_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.active = True
                form.save()
                return redirect('main:show_teams_list')
            context = {'team_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditTeamView(LoginRequiredMixin, View):
    template = 'main/team_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = TeamForm

    def get(self, request, id):
        try:
            team = get_object_or_404(Team, pk=id)
            form = self.form_class(instance=team)
            context = {'team_form': form, 'new': False, 'id': id}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            team = get_object_or_404(Team, pk=id)
            form = self.form_class(request.POST or None, instance=team)
            if form.is_valid():
                form.save()
                return redirect('main:show_teams_list')
            context = {'team_form': form, 'new': False, 'id': id}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EmployersListView(LoginRequiredMixin, View):
    template = 'main/employers_list.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            employers = Employer.objects.all().filter(deleted=False).order_by("team__priority")
            try:
                last_date = Employer.objects.values("change").latest("change")
            except Employer.DoesNotExist:
                last_date = None

            secretariat = SecretariatTelephone.objects.last()
            context = {"employers": employers, "last_date": last_date, "secretariat": secretariat}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewEmployerView(LoginRequiredMixin, View):
    template = 'main/employer_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = EmployerForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'employer_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect('main:show_employers_list')
            context = {'employer_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditEmployerView(LoginRequiredMixin, View):
    template = 'main/employer_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = EmployerForm

    def get(self, request, id):
        try:
            employer = get_object_or_404(Employer, pk=id)
            form = self.form_class(instance=employer)
            context = {'employer_form': form, 'id': id, 'new': False}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            employer = get_object_or_404(Employer, pk=id)
            form = self.form_class(request.POST or None, instance=employer)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect('main:show_employers_list')
            context = {'employer_form': form, 'id': id, 'new': False}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class CommandListView(LoginRequiredMixin, View):
    template = 'main/command.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            commands = Command.objects.all().order_by("-create_date")
            commands_len = len(commands)
            try:
                last_date = Command.objects.values("change").latest("change")
            except Command.DoesNotExist:
                last_date = None
            context = {'commands': commands, 'last_date': last_date, 'commands_len': commands_len, 'secretariat': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddCommandView(LoginRequiredMixin, View):
    template = 'main/command_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = CommandForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'command_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None, request.FILES or None)
            if request.method == "POST":
                if form.is_valid():
                    form.save()
                    return redirect('main:show_command_list')
            context = {'command_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditCommandView(LoginRequiredMixin, View):
    template = 'main/command_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = CommandForm

    def get(self, request, id):
        try:
            command = get_object_or_404(Command, pk=id)
            form = self.form_class(instance=command)
            context = {'command_form': form, 'id': id, 'new': False}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            command = get_object_or_404(Command, pk=id)
            form = self.form_class(request.POST or None, instance=command)
            if form.is_valid():
                form.save()
                return redirect('main:show_command_list')
            context = {'command_form': form, 'id': id, 'new': False}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DeleteCommandView(LoginRequiredMixin, View):
    def get(self, request, id):
        try:
            command = get_object_or_404(Command, pk=id)
            command.delete()
            return redirect("main:show_command_list")
        except Exception as e:
            logger.error("Error: %s", e)


class TelephoneListView(LoginRequiredMixin, View):
    template = 'main/telephones.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            teams = Team.objects.all().filter(active=True).order_by("priority")
            telephone_book = OrganisationTelephone.objects.all()
            secretariat = SecretariatTelephone.objects.last()
            context = {"teams": teams, "telephone_book": telephone_book, "secretariat": secretariat}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewSecretariatNumberView(LoginRequiredMixin, View):
    template = 'main/secretariat_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = SecretariatTelephoneForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'secretariat_form': form, 'new': True}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('main:show_employers_list')
            context = {'secretariat_form': form, 'new': True}
            return render(request, self.template_name, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditSecretariatNumberView(LoginRequiredMixin, View):
    template = 'main/secretariat_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = SecretariatTelephoneForm

    def get(self, request, id):
        try:
            instance = get_object_or_404(SecretariatTelephone, pk=id)
            form = self.form_class(instance=instance)
            context = {'secretariat_form': form, 'new': False, 'id': id}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            instance = get_object_or_404(SecretariatTelephone, pk=id)
            form = self.form_class(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('main:show_employers_list')
            context = {'secretariat_form': form, 'new': False, 'id': id}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DeleteSecretariatNumberView(LoginRequiredMixin, View):

    def get(self, request, id):
        try:
            instance = get_object_or_404(SecretariatTelephone, pk=id)
            instance.delete()
            return redirect('main:show_employers_list')
        except Exception as e:
            logger.error("Error: %s", e)


class AccessToModulesView(LoginRequiredMixin, View):
    template = 'main/access_modules.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            access = AccessModule.objects.all()
            commands = Command.objects.all()
            context = {"access": access, "commands": commands}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ListRegisterView(LoginRequiredMixin, View):
    template = 'main/list_register.html'
    template_error = 'main/error_site.html'
    now_year = current_year()

    def get(self, request):
        try:
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
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NecesseryFileView(LoginRequiredMixin, View):
    template = 'main/necessery_files.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            commands = Command.objects.all().order_by("-create_date")
            files = NecesseryFile.objects.all().order_by("-create_date")
            context = {'files': files, 'commands': commands}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DownloadFilesView(LoginRequiredMixin, View):
    template = 'main/download_file.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            files = NecesseryFile.objects.all().order_by('create_date')
            files_len = len(files)
            context = {'files': files, 'files_len': files_len}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddUploadFilesView(LoginRequiredMixin, View):
    template = 'main/download_file_form_popup.html'
    template_error = 'main/error_site.html'
    form_class = NecesseryFileForm

    def get(self, request):
        try:
            form = self.form_class()
            context = {'download_file_form': form}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None, request.FILES or None)
            if request.method == "POST":
                if form.is_valid():
                    form.save()
                    return redirect('main:download_files')
            context = {'download_file_form': form}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DeleteUploadFile(LoginRequiredMixin, View):
    def get(self, request, id):
        try:
            file = get_object_or_404(NecesseryFile, pk=id)
            file.delete()
            return redirect('main:download_files')
        except Exception as e:
            logger.error("Error: %s", e)
