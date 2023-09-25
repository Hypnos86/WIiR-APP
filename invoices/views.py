import logging
import datetime
import pathlib
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from invoices.models import InvoiceSell, InvoiceBuy, InvoiceItems, DocumentTypes, CorrectiveNote, DocumentsTypeEnum
from main.models import Employer
from invoices.forms import InvoiceSellForm, InvoiceBuyForm, InvoiceItemsForm, CorrectiveNoteForm
from main.views import current_year, now_date
from django.urls import reverse
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

logger = logging.getLogger(__name__)


# Create your views here.
class MenuInvoicesView(LoginRequiredMixin, View):
    template_name = "invoices/main_invoice.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            now_year = current_year()

            # Filtrowanie faktur sprzedażowych
            all_year_sell = InvoiceSell.objects.all().values("date__year").exclude(date__year=now_year)
            year_sell_set = set([year["date__year"] for year in all_year_sell])
            year_sell_list = sorted(year_sell_set, reverse=True)

            # Filtrowanie faktur przychodzących
            all_year_buy = InvoiceBuy.objects.all().values("date_receipt__year").exclude(date_receipt__year=now_year)
            year_buy_set = set([year["date_receipt__year"] for year in all_year_buy])
            year_buy_list = sorted(year_buy_set, reverse=True)

            # Filtrowanie not księgowych
            all_year_note = CorrectiveNote.objects.all().values("date__year").exclude(date__year=now_year)
            year_note_set = set([year["date__year"] for year in all_year_note])
            year_note_list = sorted(year_note_set, reverse=True)

            return render(request, self.template_name, {
                "now_year": now_year,
                "all_year_sell": year_sell_list,
                "all_year_buy": year_buy_list,
                "year_note_list": year_note_list
            })
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class BuyInvoicesListView(LoginRequiredMixin, View):
    template_name = "invoices/list_invoice_buy.html"
    template_error = 'main/error_site.html'
    paginate_by = 40

    def get(self, request):
        try:
            now_year = current_year()
            invoices_buy = InvoiceBuy.objects.all().order_by("-date_receipt").filter(date_receipt__year=now_year)
            query = "Wyczyść"
            search = "Szukaj"
            invoices_buy_sum = len(invoices_buy)
            year = current_year()
            q = request.GET.get("q")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            paginator = Paginator(invoices_buy, self.paginate_by)
            page_number = request.GET.get("page")
            invoices_buy_list = paginator.get_page(page_number)

            if q or date_from or date_to:
                if q:
                    invoices_buy = invoices_buy.filter(no_invoice__icontains=q) \
                                   | invoices_buy.filter(sum__startswith=q) \
                                   | invoices_buy.filter(contractor__name__icontains=q) \
                                   | invoices_buy.filter(contractor__no_contractor__startswith=q) \
                                   | invoices_buy.filter(invoice_items__county__name__icontains=q) \
                                   | invoices_buy.filter(invoice_items__account__section__section__icontains=q) \
                                   | invoices_buy.filter(invoice_items__account__paragraph__paragraph__icontains=q) \
                                   | invoices_buy.filter(invoice_items__account__source__source__icontains=q)

                if date_from:
                    invoices_buy = invoices_buy.filter(date_receipt__gte=date_from)

                if date_to:
                    invoices_buy = invoices_buy.filter(date_receipt__lte=date_to)

                invoices_buy_filter_sum = len(invoices_buy)
                context = {"invoices": set(invoices_buy),
                           "invoices_buy_sum": invoices_buy_filter_sum,
                           "query": query, "year": year, "q": q,
                           "date_from": date_from,
                           "date_to": date_to}
                return render(request, self.template_name, context)
            else:
                context = {"invoices": invoices_buy_list,
                           "invoices_buy_sum": invoices_buy_sum,
                           "search": search, "year": year, }
                return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowInfoBuyView(LoginRequiredMixin, View):
    template_name = "invoices/modal_info_invoice_buy.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            invoice = get_object_or_404(InvoiceBuy, pk=id)
            items = InvoiceItems.objects.filter(invoice_id=invoice)
            context = {"invoice": invoice, "items": items, "id": id}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class BuyInvoicesListArchiveView(LoginRequiredMixin, View):
    template_name = "invoices/list_archive_invoice_buy.html"
    template_error = 'main/error_site.html'
    per_page = 40

    def get(self, request, year):
        try:
            try:
                year = int(year)
            except ValueError:
                raise Http404("Invalid year")

            invoices_buy = InvoiceBuy.objects.filter(date_receipt__year=year).order_by("-date_receipt")
            query = "Wyczyść"
            search = "Szukaj"
            invoices_buy_sum = len(invoices_buy)
            q = request.GET.get("q")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            paginator = Paginator(invoices_buy, self.per_page)
            page_number = request.GET.get("page")
            invoices_buy_list = paginator.get_page(page_number)

            if q or date_from or date_to:
                if q:
                    invoicesbuy = invoices_buy.filter(no_invoice__icontains=q) \
                                  | invoices_buy.filter(sum__startswith=q) \
                                  | invoices_buy.filter(contractor__name__icontains=q) \
                                  | invoices_buy.filter(contractor__no_contractor__startswith=q) \
                                  | invoices_buy.filter(invoiceitems__county__name__icontains=q)

                if date_from:
                    invoicesbuy = invoices_buy.filter(date_receipt__gte=date_from)

                if date_to:
                    invoicesbuy = invoices_buy.filter(date_receipt__lte=date_to)

                invoices_buy_filter_sum = len(invoicesbuy)
                context = {"invoices": invoicesbuy,
                           "invoices_buy_sum": invoices_buy_filter_sum,
                           "query": query, "year": year, "q": q,
                           "date_from": date_from,
                           "date_to": date_to
                           }
                return render(request, self.template_name, context)
            else:
                context = {"invoices": invoices_buy_list, "invoices_buy_sum": invoices_buy_sum, "search": search,
                           "year": year}
                return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewInvoiceBuyView(LoginRequiredMixin, View):
    template_name = 'invoices/form_invoice_buy.html'
    template_error = 'main/error_site.html'
    form_class = InvoiceBuyForm

    def get(self, request):
        try:
            doc_types = DocumentTypes.objects.exclude(type=DocumentsTypeEnum.NOTA_KORYGUJACA.value)
            invoice_buy_form = self.form_class()
            context = {"invoice": invoice_buy_form, "doc_types": doc_types, "new": True}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            invoice_buy_form = self.form_class(request.POST or None)
            if invoice_buy_form.is_valid():
                instance = invoice_buy_form.save(commit=False)
                instance.author = request.user
                invoice_buy_form.save()
                return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": instance.id}))

            doc_types = DocumentTypes.objects.exclude(type=DocumentsTypeEnum.NOTA_KORYGUJACA.value)
            context = {"invoice": invoice_buy_form, "doc_types": doc_types, "new": True}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class AddItemsInvoiceBuyView(LoginRequiredMixin, View):
    template_name = "invoices/form_invoice_items.html"
    template_error = 'main/error_site.html'
    form_class = InvoiceItemsForm

    def get(self, request, id):
        try:
            invoice_edit = get_object_or_404(InvoiceBuy, pk=id)
            invoice_item_form = self.form_class()
            invoice_items = InvoiceItems.objects.filter(invoice_id=invoice_edit)

            context = {"invoice_item": invoice_item_form, "invoice": invoice_edit, "invoice_items": invoice_items,
                       "new": True}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            invoice_edit = get_object_or_404(InvoiceBuy, pk=id)
            invoice_item_form = self.form_class(request.POST)
            invoice_items = InvoiceItems.objects.filter(invoice_id=invoice_edit)

            context = {"invoice_item": invoice_item_form, "invoice": invoice_edit, "invoice_items": invoice_items,
                       "new": True}

            if invoice_item_form.is_valid():
                instance = invoice_item_form.save(commit=False)
                instance.invoice_id = invoice_edit
                invoice_item_form.save()

                return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": invoice_edit.id}))

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DeleteItemsInvoiceBuyView(LoginRequiredMixin, View):
    template_name = 'invoices:add_items_invoice_buy'
    template_error = 'main/error_site.html'

    def get(self, request, id, invoice_id):
        try:
            item = get_object_or_404(InvoiceItems, pk=id)
            item.delete()
            invoice = get_object_or_404(InvoiceBuy, pk=invoice_id)
            return redirect(reverse(self.template_name, kwargs={"id": invoice.id}))
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditInvoiceBuyView(LoginRequiredMixin, View):
    template_name = 'invoices/form_invoice_buy.html'
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
            invoice_buy_form = InvoiceBuyForm(instance=invoice_buy_edit)
            invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA)
            context = {"invoice": invoice_buy_form,
                       "invoice_id": invoice_buy_edit,
                       "new": False}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
            invoice_buy_form = InvoiceBuyForm(request.POST, instance=invoice_buy_edit)
            invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA)
            context = {"invoice": invoice_buy_form,
                       "invoice_id": invoice_buy_edit,
                       "new": False}

            if invoice_buy_form.is_valid():
                instance = invoice_buy_form.save(commit=False)
                instance.author = request.user
                invoice_buy_form.save()
                return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": instance.id}))

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class DeleteInvoiceBuyView(LoginRequiredMixin, View):

    def get(self, request, id):
        invoice = get_object_or_404(InvoiceBuy, pk=id)
        year = invoice.date_receipt.year
        invoice.delete()
        return redirect("invoices:buy_invoices_list", year=year)


# class EditInvoiceBuyArchiveView(View):
#     template_name = 'invoices/form_invoice_buy.html'
#
#     def get(self, request, id):
#         invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
#         invoice_buy_form = InvoiceBuyForm(instance=invoice_buy_edit)
#         invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
#             type=DocumentsTypeEnum.NOTA_KORYGUJACA)
#         year = invoice_buy_edit.date_receipt.year
#
#         context = {"invoice": invoice_buy_form,
#                    "new": False,
#                    "year": year}
#
#         return render(request, self.template_name, context)
#
#     def post(self, request, id):
#         invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
#         invoice_buy_form = InvoiceBuyForm(request.POST, instance=invoice_buy_edit)
#         invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
#             type=DocumentsTypeEnum.NOTA_KORYGUJACA)
#         year = invoice_buy_edit.date_receipt.year
#
#         context = {"invoice": invoice_buy_form,
#                    "new": False,
#                    "year": year}
#
#         if invoice_buy_form.is_valid():
#             instance = invoice_buy_form.save(commit=False)
#             instance.author = request.user
#             invoice_buy_form.save()
#             return redirect("invoices:buy_invoices_list", year=year)
#
#         return render(request, self.template_name, context)


class SellInvoicesListView(LoginRequiredMixin, View):
    template_name = "invoices/list_invoice_sell.html"  # Dodaj template_name
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            year = current_year()
            invoicesSell = InvoiceSell.objects.all().order_by("-date").filter(date__year=year)
            for invoice in invoicesSell:
                invoice.period_from = datetime.date(year=int(invoice.period_from[0:4]),
                                                    month=int(invoice.period_from[5:7]), day=1)
                invoice.period_to = datetime.date(year=int(invoice.period_to[0:4]),
                                                  month=int(invoice.period_to[5:7]), day=1)

            query = "Wyczyść"
            search = "Szukaj"
            invoices_sell_len = len(invoicesSell)
            invoices_sell_sum_dict = invoicesSell.aggregate(Sum("sum"))

            try:
                invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
            except TypeError:
                invoices_sell_sum = 0

            q = request.GET.get("q")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            paginator = Paginator(invoicesSell, 40)
            page_number = request.GET.get("page")
            invoicesSellList = paginator.get_page(page_number)

            if q or date_from or date_to:
                if q:
                    invoicesSell = invoicesSell.filter(no_invoice__icontains=q) \
                                   | invoicesSell.filter(sum__startswith=q) \
                                   | invoicesSell.filter(date__startswith=q) \
                                   | invoicesSell.filter(contractor__name__icontains=q) \
                                   | invoicesSell.filter(contractor__no_contractor__startswith=q) \
                                   | invoicesSell.filter(county__name__icontains=q) \
                                   | invoicesSell.filter(information__icontains=q) \
                                   | invoicesSell.filter(doc_types__type__icontains=q)

                if date_from:
                    invoicesSell = invoicesSell.filter(date__gte=date_from)

                if date_to:
                    invoicesSell = invoicesSell.filter(date__lte=date_to)

                invoices_sell_filter_sum = len(invoicesSell)
                invoices_sell_sum_dict = invoicesSell.aggregate(Sum("sum"))
                for invoice in invoicesSell:
                    invoice.period_from = datetime.date(year=int(invoice.period_from[0:4]),
                                                        month=int(invoice.period_from[5:7]), day=1)
                    invoice.period_to = datetime.date(year=int(invoice.period_to[0:4]),
                                                      month=int(invoice.period_to[5:7]), day=1)

                try:
                    invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
                except TypeError:
                    invoices_sell_sum = 0
                context = {"invoices": invoicesSell,
                           "invoices_sell_len": invoices_sell_filter_sum,
                           "invoices_sell_sum": invoices_sell_sum,
                           "query": query, "year": year, "q": q,
                           "date_from": date_from, "date_to": date_to}
                return render(request, self.template_name, context)
            else:
                context = {"invoices": invoicesSellList,
                           "invoices_sell_len": invoices_sell_len,
                           "invoices_sell_sum": invoices_sell_sum,
                           "search": search, "year": year}
                return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowInfoSellView(LoginRequiredMixin, View):
    template_name = "invoices/modal_info_invoice_sell.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            invoice = get_object_or_404(InvoiceSell, pk=id)
            invoice.period_from = datetime.date(year=int(invoice.period_from[0:4]),
                                                month=int(invoice.period_from[5:7]), day=1)
            invoice.period_to = datetime.date(year=int(invoice.period_to[0:4]),
                                              month=int(invoice.period_to[5:7]), day=1)

            context = {"invoice": invoice, "id": id}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class SellInvoicesListArchiveView(LoginRequiredMixin, View):
    template_name = "invoices/list_archive_invoice_sell.html"
    template_error = 'main/error_site.html'
    items_per_page = 40

    def get(self, request, year):
        try:
            invoices_sell = InvoiceSell.objects.filter(date__year=year).order_by("-date")
            for invoice in invoices_sell:
                invoice.period_from = datetime.date(year=int(invoice.period_from[0:4]),
                                                    month=int(invoice.period_from[5:7]), day=1)
                invoice.period_to = datetime.date(year=int(invoice.period_to[0:4]),
                                                  month=int(invoice.period_to[5:7]), day=1)

            invoices_sell_len = len(invoices_sell)
            invoices_sell_sum_dict = invoices_sell.aggregate(Sum("sum"))
            invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
            query = "Wyczyść"
            search = "Szukaj"
            q = request.GET.get("q")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            paginator = Paginator(invoices_sell, self.items_per_page)
            page_number = request.GET.get("page")
            invoices_sell_list = paginator.get_page(page_number)

            if q or date_from or date_to:
                if q:
                    invoices_sell = invoices_sell.filter(no_invoice__icontains=q) \
                                    | invoices_sell.filter(sum__startswith=q) \
                                    | invoices_sell.filter(date__startswith=q) \
                                    | invoices_sell.filter(contractor__name__icontains=q) \
                                    | invoices_sell.filter(contractor__no_contractor__startswith=q) \
                                    | invoices_sell.filter(county__name__icontains=q) \
                                    | invoices_sell.filter(information__icontains=q) \
                                    | invoices_sell.filter(doc_types__type__icontains=q)

                if date_from:
                    invoices_sell = invoices_sell.filter(date__gte=date_from)

                if date_to:
                    invoices_sell = invoices_sell.filter(date__lte=date_to)

                invoices_sell_filter_sum = len(invoices_sell)
                invoices_sell_sum_dict = invoices_sell.aggregate(Sum("sum"))
                try:
                    invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
                except TypeError:
                    invoices_sell_sum = 0

                context = {"invoices": invoices_sell,
                           "invoices_sell_len": invoices_sell_filter_sum,
                           "invoices_sell_sum": invoices_sell_sum,
                           "query": query, "year": year, "q": q,
                           "date_from": date_from,
                           "date_to": date_to
                           }
                return render(request, self.template_name, context)
            else:
                context = {"invoices": invoices_sell_list,
                           "invoices_sell_len": invoices_sell_len,
                           "invoices_sell_sum": invoices_sell_sum,
                           "search": search, "year": year}
                return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class NewInvoiceSellView(LoginRequiredMixin, View):
    template_name = "invoices/form_invoice_sell.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            invoice_sell_form = InvoiceSellForm()
            doc_types = invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA.value)
            invoice_sell_form.fields["creator"].queryset = Employer.objects.all().filter(invoices_issues=True)
            context = {"form": invoice_sell_form, "doc_types": doc_types, "new": True}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            invoice_sell_form = InvoiceSellForm(request.POST)
            doc_types = invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA.value)
            invoice_sell_form.fields["creator"].queryset = Employer.objects.all().filter(invoices_issues=True)
            context = {"form": invoice_sell_form, "doc_types": doc_types, "new": True}
            if invoice_sell_form.is_valid():
                instance = invoice_sell_form.save(commit=False)
                instance.author = request.user
                invoice_sell_form.save()
                return redirect("invoices:sell_invoices_list")

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditInvoiceSellView(LoginRequiredMixin, View):
    template_name = "invoices/form_invoice_sell.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
            invoice_sell_form = InvoiceSellForm(instance=invoice_sell_edit)
            invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA)
            invoice_sell_form.fields["creator"].queryset = Employer.objects.all().filter(invoices_issues=True)
            context = {"form": invoice_sell_form, "new": False}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
            invoice_sell_form = InvoiceSellForm(request.POST, instance=invoice_sell_edit)
            invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA)
            invoice_sell_form.fields["creator"].queryset = Employer.objects.all().filter(invoices_issues=True)
            context = {"form": invoice_sell_form, "new": False}

            if invoice_sell_form.is_valid():
                instance = invoice_sell_form.save(commit=False)
                instance.author = request.user
                invoice_sell_form.save()
                return redirect("invoices:sell_invoices_list")

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditInvoiceSellArchiveView(LoginRequiredMixin, View):
    template_name = "invoices/form_invoice_sell_archive.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
            invoice_sell_form = InvoiceSellForm(instance=invoice_sell_edit)
            invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA)
            year = invoice_sell_edit.date.year

            context = {"invoice": invoice_sell_form,
                       "new": False,
                       "year": year}

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
            invoice_sell_form = InvoiceSellForm(request.POST, instance=invoice_sell_edit)
            invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(
                type=DocumentsTypeEnum.NOTA_KORYGUJACA)
            year = invoice_sell_edit.date.year

            if invoice_sell_form.is_valid():
                instance = invoice_sell_form.save(commit=False)
                instance.author = request.user
                invoice_sell_form.save()
                return redirect(reverse("invoices:sell_invoices_list_archive", kwargs={"year": year}))

            context = {"invoice": invoice_sell_form,
                       "new": False,
                       "year": year}

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class CorrectiveNoteListView(LoginRequiredMixin, View):
    template_name = "invoices/list_corrective_note.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            notes = CorrectiveNote.objects.filter(date__year=current_year()).order_by("-date")
            notes_len = len(notes)
            year = current_year()
            query = "Wyczyść"
            search = "Szukaj"

            q = request.GET.get("q")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            paginator = Paginator(notes, 30)
            page_number = request.GET.get("page")
            note_list = paginator.get_page(page_number)

            if q or date_from or date_to:
                if q:
                    notes = notes.filter(no_note__icontains=q) \
                            | notes.filter(contractor__name__icontains=q) \
                            | notes.filter(corrective_invoice__icontains=q)

                if date_from:
                    notes = notes.filter(date__gte=date_from)

                if date_to:
                    notes = notes.filter(date__lte=date_to)

                notes_len = len(notes)

                return render(request, self.template_name, {"notes": notes,
                                                            "notes_len": notes_len,
                                                            "query": query, "year": year, "q": q,
                                                            "date_from": date_from, "date_to": date_to})
            else:
                return render(request, self.template_name, {"notes": note_list,
                                                            "notes_len": notes_len,
                                                            "year": year,
                                                            "search": search})
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class ShowCorrectiveNoteInfoView(LoginRequiredMixin, View):
    template_name = "invoices/modal_info_note.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            note = get_object_or_404(CorrectiveNote, pk=id)
            return render(request, self.template_name, {"note": note, "id": id})
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class CorrectiveNoteListArchiveView(LoginRequiredMixin, View):
    template_name = "invoices/list_archive_corrective_note.html"
    template_error = 'main/error_site.html'

    def get(self, request, year):
        try:
            notes = CorrectiveNote.objects.filter(date__year=year).order_by("-date")
            notes_len = len(notes)
            query = "Wyczyść"
            search = "Szukaj"

            q = request.GET.get("q")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            paginator = Paginator(notes, 30)
            page_number = request.GET.get("page")
            note_list = paginator.get_page(page_number)

            if q or date_from or date_to:
                if q:
                    notes = notes.filter(no_note__icontains=q) \
                            | notes.filter(contractor__name__icontains=q) \
                            | notes.filter(corrective_invoice__icontains=q)

                if date_from:
                    notes = notes.filter(date__gte=date_from)

                if date_to:
                    notes = notes.filter(date__lte=date_to)

                notes_len = len(notes)
                context = {"notes": notes,
                           "notes_len": notes_len,
                           "query": query, "year": year, "q": q,
                           "date_from": date_from,
                           "date_to": date_to}
                return render(request, self.template_name, context)
            else:
                context = {"notes": note_list, "notes_len": notes_len, "year": year, "search": search}
                return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class CorrectiveNoteCreateView(View):
    template_name = "invoices/form_corrective_note.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            note_form = CorrectiveNoteForm()
            context = {"note_form": note_form, "new": True}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            note_form = CorrectiveNoteForm(request.POST)
            context = {"note_form": note_form, "new": True}

            if note_form.is_valid():
                instance = note_form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect("invoices:corrective_note_list")

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class CorrectiveNoteUpdateView(LoginRequiredMixin, View):
    template_name = "invoices/form_corrective_note.html"
    template_error = 'main/error_site.html'

    def get(self, request, id):
        try:
            note = get_object_or_404(CorrectiveNote, pk=id)
            note_form = CorrectiveNoteForm(instance=note)
            context = {"note_form": note_form, "new": False}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            note = get_object_or_404(CorrectiveNote, pk=id)
            note_form = CorrectiveNoteForm(request.POST, instance=note)
            context = {"note_form": note_form, "new": False}

            if note_form.is_valid():
                instance = note_form.save(commit=False)
                instance.author = request.user
                note_form.save()
                return redirect("invoices:corrective_note_list")

            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class EditNoteArchiveView(LoginRequiredMixin, View):
    template_name = "invoices/form_corrective_note_archive.html"
    template_error = 'main/error_site.html'
    class_form = CorrectiveNoteForm

    def get(self, request, id):
        try:
            note = get_object_or_404(CorrectiveNote, pk=id)
            form = self.class_form(instance=note)
            year = note.date.year
            context = {"note_form": form, "year": year}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    def post(self, request, id):
        try:
            note = get_object_or_404(CorrectiveNote, pk=id)
            form = self.class_form(request.POST or None, instance=note)
            year = note.date.year
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                form.save()
                return redirect(reverse("invoices:corrective_note_list_archive", kwargs={"year": year}))
            context = {"note_form": form, "year": year}
            return render(request, self.template_name, context)
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class MakeVerificationView(LoginRequiredMixin, View):
    template_name = "invoices/verification.html"
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            invoices_buy = InvoiceBuy.objects.all().order_by("date_of_payment")
            query = "Wyczyść"
            search = "Szukaj"
            year = current_year()
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            if date_from:
                date_from_obj = datetime.datetime.strptime(date_from, "%Y-%m-%d")
            else:
                date_from_obj = None

            if date_to:
                date_to_obj = datetime.datetime.strptime(date_to, "%Y-%m-%d")
            else:
                date_to_obj = None

            if date_from and date_to:

                invoices_buy_list = invoices_buy.filter(date_of_payment__range=[date_from, date_to])

                days = set([days["date_of_payment"] for days in invoices_buy_list.values("date_of_payment", "sum")])

                day_sum = {}
                for day in days:
                    sum = 0
                    for invoice in invoices_buy_list:
                        if day == invoice.date_of_payment:
                            sum += invoice.sum
                    day_sum[day] = sum
                invoices_buy_sum = len(invoices_buy_list)

                try:
                    verification_all_dict = invoices_buy_list.aggregate(Sum("sum"))
                    verification_all = round(verification_all_dict["sum__sum"], 2)
                except TypeError:
                    verification_all = 0

                return render(request, self.template_name, {"invoices": invoices_buy_list,
                                                            "invoices_buy_sum": invoices_buy_sum,
                                                            "query": query, "year": year,
                                                            "date_from": date_from,
                                                            "date_to": date_to,
                                                            "day_sum": day_sum,
                                                            "date_from_obj": date_from_obj,
                                                            "date_to_obj": date_to_obj,
                                                            "verification_all": verification_all})
            else:
                invoices_buy_sum = 0
                return render(request, self.template_name, {
                    "invoices_buy_sum": invoices_buy_sum,
                    "search": search, "year": year
                })
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)


class MakePDFFromInvoicesSellView(View):
    template_name = "invoices/pdf_invoice_sell.html"
    template_error = 'main/error_site.html'

    def get(self, request, year):
        try:
            q = request.GET.get("q", "")
            date_from = request.GET.get("from")
            date_to = request.GET.get("to")

            invoicessell = InvoiceSell.objects.all().order_by("-date").filter(date__year=year)
            invoices_sell_sum_dict = invoicessell.aggregate(Sum("sum"))
            user = request.user
            try:
                invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
            except TypeError:
                invoices_sell_sum = 0

            now = now_date()

            if q or date_from or date_to:
                if q:
                    invoicessell = invoicessell.filter(no_invoice__icontains=q) \
                                   | invoicessell.filter(sum__startswith=q) \
                                   | invoicessell.filter(date__startswith=q) \
                                   | invoicessell.filter(contractor__name__icontains=q) \
                                   | invoicessell.filter(contractor__no_contractor__startswith=q) \
                                   | invoicessell.filter(county__name__icontains=q) \
                                   | invoicessell.filter(creator__id_swop__icontains=q) \
                                   | invoicessell.filter(information__icontains=q)

                if date_from:
                    invoicessell = invoicessell.filter(date__gte=date_from)

                if date_to:
                    invoicessell = invoicessell.filter(date__lte=date_to)

                invoices_sell_sum_dict = invoicessell.aggregate(Sum("sum"))

                try:
                    invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
                except TypeError:
                    invoices_sell_sum = 0

            objects = range(1, len(invoicessell) + 1)
            invoicessell = zip(objects, invoicessell)

            # Get base dir for font directory
            base_dir = settings.BASE_DIR

            relative_dir = pathlib.Path('/invoices/templates/invoices/fonts/roboto/Roboto-Light.ttf')

            font_dir = str(base_dir.absolute()) + str(relative_dir)

            context = {"invoices": invoicessell, "date_from": date_from,
                       "date_to": date_to, "invoices_sell_sum": invoices_sell_sum, "now": now, "year": year,
                       "invoices_sell_sum_dict": invoices_sell_sum_dict, "objects": objects, "user": user,
                       "font_dir": font_dir}

            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type="application/pdf")
            now_time = now.strftime("%d-%m-%Y")
            response[
                "Content-Disposition"] = "attachment; filename=Lista wystawionych faktur - utworzono {now_time}.pdf".format(
                now_time=now_time)
            # Find the template and render it.
            template_path = self.template_name
            template = get_template(template_path)
            html = template.render(context)

            # Create a PDF
            pisa_status = pisa.CreatePDF(html, dest=response, encoding="UTF-8", link_callback=self.link_callback)

            # If there's an error, return an error response
            if pisa_status.err:
                return HttpResponse("Wystąpił jakiś problem :( Error:997 <pre>" + html + "</pre>")

            return response
        except Exception as e:
            # Zapisanie informacji o błędzie do loga
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)

    @staticmethod
    def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # Make sure that the file exists
        if not os.path.isfile(path):
            raise Exception('Media URI must start with %s or %s' % (sUrl, mUrl))
        return path
