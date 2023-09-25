import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from .models import NeedsLetter, TeamType, RegistrationType
from .forms import NeedsLetterForm
from main.models import Employer
from units.models import Unit
from main.views import current_year

logger = logging.getLogger(__name__)


# Create your views here.

class NeedsLetterListView(LoginRequiredMixin, View):
    template = "operationalneedsrecords/needs_letter_list.html"
    template_error = 'main/error_site.html'

    def get(self, request, year):
        try:
            objects = NeedsLetter.objects.all().filter(receipt_date__year=year, isDone=False).order_by("-receipt_date")
            objectslen = len(objects)
            now_year = current_year()
            query = "Wyczyść"
            search = "Szukaj"
            q = request.GET.get("q")

            paginator = Paginator(objects, 50)
            page_number = request.GET.get('page')
            objects_list = paginator.get_page(page_number)

            try:
                last_date = NeedsLetter.objects.values('change').latest('change')
            except NeedsLetter.DoesNotExist:
                last_date = None

            now_year_str = now_year
            if year == str(now_year_str):
                oldYear = False
            else:
                oldYear = True

            if q:
                objects = objects.filter(case_sign__icontains=q) \
                          | objects.filter(unit__county__name__icontains=q) \
                          | objects.filter(unit__city__icontains=q) \
                          | objects.filter(case_type__metric_type__icontains=q) \
                          | objects.filter(registration_type__registration_type__icontains=q) \
                          | objects.filter(employer__name__icontains=q) \
                          | objects.filter(employer__last_name__icontains=q) \
                          | objects.filter(no_secretariats_diary__icontains=q)
                context = {"objects": objects, "last_date": last_date, "objectslen": objectslen,
                           "year": year, "q": q, 'query': query, "archive": False, 'old_year': oldYear,
                           'now_year': now_year}
                return render(request, self.template, context
                              )

            else:
                context = {"objects": objects_list, "last_date": last_date, "objectslen": objectslen, 'search': search,
                           "year": year, "q": q, "archive": False, 'isFromShow': False,
                           'old_year': oldYear, 'now_year': now_year}
                return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NeedsLetterArchiveView(LoginRequiredMixin, View):
    template = "operationalneedsrecords/needs_letter_list.html"
    template_error = 'main/error_site.html'

    def get(self, request, year):
        try:
            objects = NeedsLetter.objects.all().filter(receipt_date__year=year, isDone=True).order_by("-receipt_date")
            objectslen = len(objects)
            now_year = current_year()

            query = "Wyczyść"
            search = "Szukaj"
            q = request.GET.get("q")

            paginator = Paginator(objects, 50)
            page_number = request.GET.get('page')
            objects_list = paginator.get_page(page_number)

            try:
                last_date = NeedsLetter.objects.values('change').latest('change')
            except NeedsLetter.DoesNotExist:
                last_date = None

            now_year_str = now_year
            if year == str(now_year_str):
                oldYear = False
            else:
                oldYear = True

            if q:
                objects = objects.filter(case_sign__icontains=q) \
                          | objects.filter(unit__county__name__icontains=q) \
                          | objects.filter(unit__city__icontains=q) \
                          | objects.filter(case_type__metric_type__icontains=q) \
                          | objects.filter(registration_type__registration_type__icontains=q) \
                          | objects.filter(employer__name__icontains=q) \
                          | objects.filter(employer__last_name__icontains=q) \
                          | objects.filter(no_secretariats_diary__icontains=q)

                context = {"objects": objects, "last_date": last_date, "objectslen": objectslen, "query": query,
                           "year": year, "archive": True, "now_year": now_year, 'old_year': oldYear}
                return render(request, self.template, context)
            else:
                context = {"objects": objects_list, "last_date": last_date, "objectslen": objectslen, "search": search,
                           "year": year, "archive": True, "now_year": now_year, 'old_year': oldYear}
                return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewNeedsLetterView(View):
    template = "operationalneedsrecords/needs_letter_form.html"
    template_error = 'main/error_site.html'

    def get(self, request, year):
        try:
            object_form = NeedsLetterForm()
            object_form.fields['employer'].queryset = Employer.objects.filter(team=TeamType.ZE.value)
            units = Unit.objects.all()
            context = {"object_form": object_form, "units": units, "new": True, "year": year}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, year):
        try:
            object_form = NeedsLetterForm(request.POST)
            object_form.fields['employer'].queryset = Employer.objects.filter(team=TeamType.ZE.value)
            units = Unit.objects.all()
            if object_form.is_valid():
                instance = object_form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect(reverse('operationalneedsrecords:list_needs_letter', kwargs={"year": year}))
            context = {"object_form": object_form, "units": units, "new": True, "year": year}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditNeedsLetterView(View):
    template = "operationalneedsrecords/needs_letter_form.html"
    template_error = 'main/error_site.html'

    def get(self, request, year, id, isFromShow=None):
        try:
            object_letter = get_object_or_404(NeedsLetter, pk=id)
            object_form = NeedsLetterForm(instance=object_letter)
            object_form.fields['employer'].queryset = Employer.objects.filter(team=TeamType.ZE.value)
            units = Unit.objects.all()
            object_edit = object_letter.unit
            context = {"object_form": object_form, "units": units, "object_edit": object_edit, "new": False,
                       "year": year, "id": id, "isFromShow": isFromShow}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, year, id, isFromShow=None):
        try:
            object_letter = get_object_or_404(NeedsLetter, pk=id)
            object_form = NeedsLetterForm(request.POST, instance=object_letter)
            object_form.fields['employer'].queryset = Employer.objects.filter(team=TeamType.ZE.value)
            units = Unit.objects.all()
            object_edit = object_letter.unit
            if object_form.is_valid():
                instance = object_form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect(reverse('operationalneedsrecords:list_needs_letter', kwargs={"year": year}))
            context = {"object_form": object_form, "units": units, "object_edit": object_edit, "new": False,
                       "year": year, "id": id, "isFromShow": isFromShow}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowNeedsLetterView(LoginRequiredMixin, View):
    template = "operationalneedsrecords/needs_letter_show.html"
    template_error = 'main/error_site.html'

    def get(self, request, year, id):
        try:
            obj = get_object_or_404(NeedsLetter, pk=id)
            if obj.receipt_date.year != current_year():
                archive = True
            else:
                archive = False
            context = {"object": obj, "year": year, "isFromShow": True, "archive": archive}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ArchiveYearListView(LoginRequiredMixin, View):
    template = "operationalneedsrecords/archive_list_year.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            now_year = current_year()
            # Filtrowanie pism

            all_year_order = NeedsLetter.objects.all().values('receipt_date__year').exclude(receipt_date__year=now_year)
            year_order_set = set([year['receipt_date__year'] for year in all_year_order])
            year_order_list = sorted(year_order_set, reverse=True)
            context = {'year_order_list': year_order_list}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


def myFunc(e):
    return e["county"].name


class StatisticView(LoginRequiredMixin, View):
    template = "operationalneedsrecords/statistics.html"
    template_error = 'main/error_site.html'

    def get(self, request, year):
        try:
            documents = NeedsLetter.objects.all().filter(receipt_date__year=year).order_by("unit__county__name")
            registrationTypes = RegistrationType.objects.all()

            counts = []
            employers_set = set()
            county_set = set()

            # Zliczanie kosztów z całego roku i tworzenie zbiorów aktywnych branżystów
            for doc in documents:
                counts.append(doc.cost)
                employer = doc.employer
                employers_set.add(employer)
                county_list = doc.unit.county
                county_set.add(county_list)

            count_all = sum(counts)
            emplo_list = []

            # Zliczanie zrealizowanych spraw przez branżystów
            for emplo in employers_set:
                docsObject = documents.filter(employer=emplo)
                sumObject = 0
                objectCouned = docsObject.count()
                sumObject += objectCouned
                newObjectEmplo = {'employer': emplo, 'caseCount': sumObject}
                emplo_list.append(newObjectEmplo)

            registrationTypeList = []

            # Zliczanie kosztów i ilości spraw
            for registrationType in registrationTypes:
                docsObjects = documents.filter(registration_type__id=registrationType.id)
                sum_type = 0
                for docsobject in docsObjects:
                    sum_type += docsobject.cost
                newObjectType = {"type": registrationType, "sumType": sum_type, 'countType': len(docsObjects)}
                registrationTypeList.append(newObjectType)

            county_info_list = []
            # Zliczanie ilości spraw, koszty i rodzaj sorawy na powiaty
            for county in county_set:
                docsObjects = documents.filter(unit__county__name=county)

                for registrationType in registrationTypes:
                    sum_type = 0

                    filterObjectTypes = docsObjects.filter(registration_type__id=registrationType.id)

                    for docObject in filterObjectTypes:
                        sum_type += docObject.cost

                    infoObject = {"county": county, "types": registrationType, "sum": sum_type,
                                  "countType": len(filterObjectTypes)}
                    county_info_list.append(infoObject)
            context = {'year': year, 'docs': documents, "count_all": count_all, "registrationTypes": registrationTypes,
                       "registrationTypeList": registrationTypeList, 'emplo_list': emplo_list,
                       'county_info_list': sorted(county_info_list, key=myFunc)}
            return render(request, self.template, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
