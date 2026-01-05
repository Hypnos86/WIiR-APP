import logging
from dateutil.relativedelta import relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views import View
from investments.models import Project
from investments.forms import ProjectForm
from units.models import Unit
from contracts.models import ContractAuction
from contracts.models import GuaranteeSettlement
from main.models import Employer
from main.views import now_date

logger = logging.getLogger(__name__)


# Create your views here.

class ImportantTaskInvestments(LoginRequiredMixin, View):
    template = "investments/investments_main.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            future_datetime = now_date() + relativedelta(months=2)
            future_date = future_datetime.date()

            settlements_all = GuaranteeSettlement.objects.all().filter(affirmation_settlement=False).filter(
                deadline_settlement__lt=future_date)
            context = {"settlements": settlements_all}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class InvestmentProjectsList(LoginRequiredMixin, View):
    template = "investments/investments_projects.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            projects = Project.objects.all().order_by("-date_of_acceptance")
            projects_sum = len(projects)
            query = "Wyczyść"
            search = "Szukaj"

            paginator = Paginator(projects, 40)
            page_number = request.GET.get("page")
            projects_lis = paginator.get_page(page_number)

            q = request.GET.get("q")

            try:
                last_date = Project.objects.values("change").latest("change")
            except Project.DoesNotExist:
                last_date = None

            if q:
                projects = projects.filter(project_title__icontains=q) \
                           | projects.filter(unit__county__name__icontains=q) \
                           | projects.filter(unit__type__type_full__icontains=q) \
                           | projects.filter(unit__city__icontains=q) \
                           | projects.filter(section__section__startswith=q) \
                           | projects.filter(source_financing__icontains=q) \
                           | projects.filter(date_of_acceptance__year__contains=q)

                projects_sum = len(projects)
                context = {"projects": projects,
                           "query": query,
                           "last_date": last_date,
                           "projects_sum": projects_sum, "q": q}
                return render(request, self.template, context)
            else:
                context = {"projects": projects_lis,
                           "search": search,
                           "last_date": last_date,
                           "projects_sum": projects_sum}
                return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddProjectView(LoginRequiredMixin, View):
    template = "investments/project_form.html"
    template_error = 'main/error_site.html'
    form_class = ProjectForm
    units = Unit.objects.all().order_by("county__id_order")
    redirect = "investments:investment_projects_list"

    def get(self, request):
        try:
            form = self.form_class()
            context = {"project_form": form,
                       "units": self.units,
                       "new": True}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.form_class(request.POST or None, request.FILES or None)
            form.fields["worker"].queryset = Employer.objects.filter(industry_specialist=True)
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.author = request.user
                    form.save()
                    return redirect(self.redirect)
            context = {"project_form": form, "units": self.units, "new": True
                       }
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditProjectView(LoginRequiredMixin, View):
    template = "investments/project_form.html"
    template_error = 'main/error_site.html'
    form_class = ProjectForm
    units = Unit.objects.all().order_by("county__id_order")
    redirect = "investments:investment_projects_list"

    def get(self, request, id):
        try:
            project = get_object_or_404(Project, pk=id)
            form = self.form_class(instance=project)
            form.fields["worker"].queryset = Employer.objects.all().filter(industry_specialist=True)
            unit_edit = project.unit
            context = {"project_form": form, "units": self.units, "project": project, "unit_edit": unit_edit,
                       "new": False}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            project = get_object_or_404(Project, pk=id)
            form = self.form_class(request.POST or None, request.FILES or None, instance=project)
            form.fields["worker"].queryset = Employer.objects.all().filter(industry_specialist=True)
            unit_edit = project.unit
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.author = request.user
                    form.save()
                    return redirect(self.redirect)
                context = {"project_form": form, "units": self.units, "project": project, "unit_edit": unit_edit,
                           "new": False}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowProjectView(LoginRequiredMixin, View):
    template = "investments/show_project.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            project = Project.objects.get(pk=id)
            galleries = project.gallery.all()
            # contracts = project.contract_auction.all()
            contracts = ContractAuction.objects.filter(investments_project=id)
            context = {"project_form": project,
                       "contracts": contracts,
                       "galleries": galleries
                       }
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowGalleriesView(LoginRequiredMixin, View):
    template = "investments/show_galleries_popup.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            project = Project.objects.get(pk=id)
            galleries = project.gallery.all()
            context = {"id": id,
                       "galleries": galleries}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddContractToProject(LoginRequiredMixin, View):
    template = "investments/add_contract_to_project_form.html"
    template_error = 'main/error_site.html'
    redirect = "investments:edit_project"

    def get(self, request, id):
        try:
            # project = get_object_or_404(Project, pk=id)
            contracts = ContractAuction.objects.filter(investments_project=None)
            context = {"contracts": contracts, "project_id": id}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            project = get_object_or_404(Project, pk=id)
            selected_contract = request.POST.get("choice")
            if selected_contract:
                contract = get_object_or_404(ContractAuction, pk=selected_contract)
                contract.investments_project = project
                contract.save()
            return redirect(reverse(self.redirect, kwargs={"id": id}))
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
