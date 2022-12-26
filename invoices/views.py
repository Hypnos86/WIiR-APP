import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from invoices.models import InvoiceSell, InvoiceBuy, InvoiceItems, DocumentTypes, CorrectiveNote
from main.models import Employer
from invoices.forms import InvoiceSellForm, InvoiceBuyForm, InvoiceItemsForm, CorrectiveNoteForm
from main.views import current_year, now_date
from django.urls import reverse
from decimal import Decimal
from django.core.exceptions import ValidationError
# xhtml2pdf
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.contrib.staticfiles import finders


# Create your views here.
@login_required
def menu_invoices(request):
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

    return render(request, "invoices/invoices_menu.html",
                  {"now_year": now_year, "all_year_sell": year_sell_list,
                   "all_year_buy": year_buy_list,
                   "year_note_list": year_note_list})


@login_required
def buy_invoices_list(request):
    invoices_buy = InvoiceBuy.objects.all().order_by("-date_receipt").filter(date_receipt__year=current_year())
    query = "Wyczyść"
    search = "Szukaj"
    invoices_buy_sum = len(invoices_buy)
    year = current_year()
    q = request.GET.get("q")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    paginator = Paginator(invoices_buy, 40)
    page_number = request.GET.get("page")
    invoices_buy_list = paginator.get_page(page_number)

    if q or date_from or date_to:
        if q:
            invoicesbuy = invoices_buy.filter(no_invoice__icontains=q) \
                          | invoices_buy.filter(sum__startswith=q) \
                          | invoices_buy.filter(contractor__name__icontains=q) \
                          | invoices_buy.filter(contractor__no_contractor__startswith=q) \
                          | invoices_buy.filter(invoice_items__county__name__icontains=q) \
                          | invoices_buy.filter(invoice_items__account__section__section__icontains=q) \
                          | invoices_buy.filter(invoice_items__account__paragraph__paragraph__icontains=q) \
                          | invoices_buy.filter(invoice_items__account__source__source__icontains=q)

        if date_from:
            invoicesbuy = invoices_buy.filter(date_receipt__gte=date_from)

        if date_to:
            invoicesbuy = invoices_buy.filter(date_receipt__lte=date_to)

        invoices_buy_filter_sum = len(invoicesbuy)
        return render(request, "invoices/invoices_buy_list.html", {"invoices": set(invoicesbuy),
                                                                   "invoices_buy_sum": invoices_buy_filter_sum,
                                                                   "query": query, "year": year, "q": q,
                                                                   "date_from": date_from,
                                                                   "date_to": date_to
                                                                   })
    else:
        return render(request, "invoices/invoices_buy_list.html", {"invoices": invoices_buy_list,
                                                                   "invoices_buy_sum": invoices_buy_sum,
                                                                   "search": search, "year": year,
                                                                   })


@login_required
def show_info_buy(request, id):
    invoice = get_object_or_404(InvoiceBuy, pk=id)
    items = InvoiceItems.objects.filter(invoice_id=invoice)
    return render(request, "invoices/info_buy_popup.html", {"invoice": invoice, "items": items, "id": id})


@login_required
def buy_invoices_list_archive(request, year):
    invoices_buy = InvoiceBuy.objects.all().filter(date_receipt__year=year).order_by("-date_receipt")
    query = "Wyczyść"
    search = "Szukaj"
    invoices_buy_sum = len(invoices_buy)
    q = request.GET.get("q")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    paginator = Paginator(invoices_buy, 40)
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
        return render(request, "invoices/invoices_buy_list_archive.html", {"invoices": invoicesbuy,
                                                                           "invoices_buy_sum": invoices_buy_filter_sum,
                                                                           "query": query, "year": year, "q": q,
                                                                           "date_from": date_from,
                                                                           "date_to": date_to
                                                                           })
    else:
        return render(request, "invoices/invoices_buy_list_archive.html", {"invoices": invoices_buy_list,
                                                                           "invoices_buy_sum": invoices_buy_sum,
                                                                           "search": search, "year": year,
                                                                           })


@login_required
def new_invoice_buy(request):
    invoice_buy_form = InvoiceBuyForm(request.POST or None)
    doc_types = invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    context = {"invoice": invoice_buy_form, "doc_types": doc_types, "new": True}

    if request.method == "POST":
        if invoice_buy_form.is_valid():
            instance = invoice_buy_form.save(commit=False)
            instance.author = request.user
            invoice_buy_form.save()
            return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": instance.id}))
    return render(request, "invoices/invoice_buy_form.html", context)


@login_required
def add_items_invoice_buy(request, id):
    invoice_edit = get_object_or_404(InvoiceBuy, pk=id)
    invoice_item_form = InvoiceItemsForm(request.POST or None)
    invoice_items = InvoiceItems.objects.filter(invoice_id=invoice_edit)

    context = {"invoice_item": invoice_item_form, "invoice": invoice_edit, "invoice_items": invoice_items, "new": True}
    if request.method == "POST":
        if invoice_item_form.is_valid():
            instance = invoice_item_form.save(commit=False)
            instance.invoice_id = invoice_edit
            invoice_item_form.save()

            return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": invoice_edit.id}))
    return render(request, "invoices/invoice_items.html", context)


@login_required
def delete_items_invoice_buy(request, id, invoice_id):
    item = get_object_or_404(InvoiceItems, pk=id)
    item.delete()
    invoice = get_object_or_404(InvoiceBuy, pk=invoice_id)
    return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": invoice.id}))


@login_required
def edit_invoice_buy(request, id):
    invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
    invoice_buy_form = InvoiceBuyForm(request.POST or None, instance=invoice_buy_edit)
    invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    context = {"invoice": invoice_buy_form,
               "invoice_id": invoice_buy_edit,
               "new": False}

    if invoice_buy_form.is_valid():
        instance = invoice_buy_form.save(commit=False)
        instance.author = request.user
        invoice_buy_form.save()
        return redirect(reverse("invoices:add_items_invoice_buy", kwargs={"id": instance.id}))
    return render(request, "invoices/invoice_buy_form.html", context)


@login_required
def delete_invoice_buy(request, id):
    invoice = get_object_or_404(InvoiceBuy, pk=id)
    invoice.delete()
    return redirect("invoices:buy_invoices_list")


@login_required
def edit_invoice_buy_archive(request, id):
    invoice_buy_edit = get_object_or_404(InvoiceBuy, pk=id)
    invoice_buy_form = InvoiceBuyForm(request.POST or None, instance=invoice_buy_edit)
    invoice_buy_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    year = invoice_buy_edit.date_receipt.year

    context = {"invoice": invoice_buy_form,
               "new": False,
               "year": year}

    if invoice_buy_form.is_valid():
        instance = invoice_buy_form.save(commit=False)
        instance.author = request.user
        invoice_buy_form.save()
        return redirect(reverse("invoices:buy_invoices_list", kwargs={"year": year}))
    return render(request, "invoices/invoice_buy_form.html", context)


@login_required
def sell_invoices_list(request):
    invoicessell = InvoiceSell.objects.all().order_by("-date").filter(date__year=current_year())
    query = "Wyczyść"
    search = "Szukaj"
    invoices_sell_len = len(invoicessell)
    invoices_sell_sum_dict = invoicessell.aggregate(Sum("sum"))

    try:
        invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
    except TypeError:
        invoices_sell_sum = 0

    year = current_year()
    q = request.GET.get("q")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    paginator = Paginator(invoicessell, 40)
    page_number = request.GET.get("page")
    invoicessell_list = paginator.get_page(page_number)

    if q or date_from or date_to:
        if q:
            invoicessell = invoicessell.filter(no_invoice__icontains=q) \
                           | invoicessell.filter(sum__startswith=q) \
                           | invoicessell.filter(date__startswith=q) \
                           | invoicessell.filter(contractor__name__icontains=q) \
                           | invoicessell.filter(contractor__no_contractor__startswith=q) \
                           | invoicessell.filter(county__name__icontains=q) \
                           | invoicessell.filter(information__icontains=q) \
                           | invoicessell.filter(doc_types__type__icontains=q)

        if date_from:
            invoicessell = invoicessell.filter(date__gte=date_from)

        if date_to:
            invoicessell = invoicessell.filter(date__lte=date_to)

        invoices_sell_filter_sum = len(invoicessell)
        invoices_sell_sum_dict = invoicessell.aggregate(Sum("sum"))

        try:
            invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
        except TypeError:
            invoices_sell_sum = 0

        return render(request, "invoices/invoices_sell_list.html", {"invoices": invoicessell,
                                                                    "invoices_sell_len": invoices_sell_filter_sum,
                                                                    "invoices_sell_sum": invoices_sell_sum,
                                                                    "query": query, "year": year, "q": q,
                                                                    "date_from": date_from, "date_to": date_to})
    else:
        return render(request, "invoices/invoices_sell_list.html", {"invoices": invoicessell_list,
                                                                    "invoices_sell_len": invoices_sell_len,
                                                                    "invoices_sell_sum": invoices_sell_sum,
                                                                    "search": search, "year": year})


@login_required
def show_info_sell(request, id):
    invoice = get_object_or_404(InvoiceSell, pk=id)
    return render(request, "invoices/info_sell_popup.html", {"invoice": invoice, "id": id})


@login_required
def sell_invoices_list_archive(request, year):
    invoices_sell = InvoiceSell.objects.all().filter(date__year=year).order_by("-date")
    invoices_sell_len = len(invoices_sell)
    invoices_sell_sum_dict = invoices_sell.aggregate(Sum("sum"))
    invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
    query = "Wyczyść"
    search = "Szukaj"
    q = request.GET.get("q")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    paginator = Paginator(invoices_sell, 40)
    page_number = request.GET.get("page")
    invoicessell_list = paginator.get_page(page_number)

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

        return render(request, "invoices/invoices_sell_list_archive.html", {"invoices": invoices_sell,
                                                                            "invoices_sell_len": invoices_sell_filter_sum,
                                                                            "invoices_sell_sum": invoices_sell_sum,
                                                                            "query": query, "year": year, "q": q,
                                                                            "date_from": date_from, "date_to": date_to})
    else:
        return render(request, "invoices/invoices_sell_list_archive.html", {"invoices": invoicessell_list,
                                                                            "invoices_sell_len": invoices_sell_len,
                                                                            "invoices_sell_sum": invoices_sell_sum,
                                                                            "search": search, "year": year})


@login_required
def new_invoice_sell(request):
    invoice_sell_form = InvoiceSellForm(request.POST or None)
    doc_types = invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    invoice_sell_form.fields["creator"].queryset = Employer.objects.all().filter(invoices_issues=True)

    context = {"invoice": invoice_sell_form, "doc_types": doc_types, "new": True}

    if request.method == "POST":
        if invoice_sell_form.is_valid():
            instance = invoice_sell_form.save(commit=False)
            instance.author = request.user
            invoice_sell_form.save()
            return redirect("invoices:sell_invoices_list")
    return render(request, "invoices/invoice_sell_form.html", context)


@login_required
def edit_invoice_sell(request, id):
    invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
    invoice_sell_form = InvoiceSellForm(request.POST or None, instance=invoice_sell_edit)
    invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    invoice_sell_form.fields["creator"].queryset = Employer.objects.all().filter(invoices_issues=True)

    context = {"invoice": invoice_sell_form,
               "new": False}

    if invoice_sell_form.is_valid():
        instance = invoice_sell_form.save(commit=False)
        instance.author = request.user
        invoice_sell_form.save()
        return redirect("invoices:sell_invoices_list")
    return render(request, "invoices/invoice_sell_form.html", context)


@login_required
def edit_invoice_sell_archive(request, id):
    invoice_sell_edit = get_object_or_404(InvoiceSell, pk=id)
    invoice_sell_form = InvoiceSellForm(request.POST or None, instance=invoice_sell_edit)
    invoice_sell_form.fields["doc_types"].queryset = DocumentTypes.objects.exclude(type="Nota korygująca")
    year = invoice_sell_edit.date.year

    context = {"invoice": invoice_sell_form,
               "new": False,
               "year": year}

    if invoice_sell_form.is_valid():
        instance = invoice_sell_form.save(commit=False)
        instance.author = request.user
        invoice_sell_form.save()
        return redirect(reverse("invoices:sell_invoices_list_archive", kwargs={"year": year}))

    return render(request, "invoices/invoice_sell_archive_form.html", context)


@login_required
def corrective_note_list(request):
    notes = CorrectiveNote.objects.all().filter(date__year=current_year()).order_by("-date")
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

        return render(request, "invoices/corrective_note_list.html", {"notes": notes,
                                                                      "notes_len": notes_len,
                                                                      "query": query, "year": year, "q": q,
                                                                      "date_from": date_from, "date_to": date_to})
    else:
        return render(request, "invoices/corrective_note_list.html", {"notes": note_list,
                                                                      "notes_len": notes_len,
                                                                      "year": year,
                                                                      "search": search})


@login_required
def show_info_note(request, id):
    note = get_object_or_404(CorrectiveNote, pk=id)
    return render(request, "invoices/info_note_popup.html", {"note": note, "id": id})


@login_required
def corrective_note_list_archive(request, year):
    notes = CorrectiveNote.objects.all().filter(date__year=year).order_by("-date")
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

        return render(request, "invoices/corrective_note_list_archive.html", {"notes": notes,
                                                                              "note_len": notes_len,
                                                                              "query": query, "year": year, "q": q,
                                                                              "date_from": date_from,
                                                                              "date_to": date_to})
    else:
        return render(request, "invoices/corrective_note_list_archive.html",
                      {"notes": note_list, "notes_len": notes_len, "year": year, "search": search})


@login_required
def new_note(request):
    note_form = CorrectiveNoteForm(request.POST or None)
    context = {"note_form": note_form, "new": True}

    if request.method == "POST":
        if note_form.is_valid():
            instance = note_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("invoices:corrective_note_list")
    return render(request, "invoices/corrective_note_form.html", context)


@login_required
def edit_note(request, id):
    note = get_object_or_404(CorrectiveNote, pk=id)
    note_form = CorrectiveNoteForm(request.POST or None, instance=note)
    context = {"note_form": note_form,
               "new": False}

    if note_form.is_valid():
        instance = note_form.save(commit=False)
        instance.author = request.user
        note_form.save()
        return redirect("invoices:corrective_note_list")
    return render(request, "invoices/corrective_note_form.html", context)


@login_required
def edit_note_archive(request, id):
    note = get_object_or_404(CorrectiveNote, pk=id)
    note_form = CorrectiveNoteForm(request.POST or None, instance=note)
    year = note.date.year
    context = {"note_form": note_form,
               "year": year}

    if note_form.is_valid():
        instance = note_form.save(commit=False)
        instance.author = request.user
        note_form.save()
        return redirect(reverse("invoices:corrective_note_list_archive", kwargs={"year": year}))
    return render(request, "invoices/corrective_note_archive_form.html", context)


@login_required
def make_verification(request):
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

        # set([year["date__year"] for year in all_year_sell])

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

        return render(request, "invoices/verification.html", {"invoices": invoices_buy_list,
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
        return render(request, "invoices/verification.html", {
            "invoices_buy_sum": invoices_buy_sum,
            "search": search, "year": year
        })


@login_required
def make_pdf_from_invoices_sell(request):
    invoicessell = InvoiceSell.objects.all().order_by("-date").filter(date__year=current_year())
    invoices_sell_sum_dict = invoicessell.aggregate(Sum("sum"))
    user = request.user
    # TODO dokończyć tworzenie pdfa
    try:
        invoices_sell_sum = round(invoices_sell_sum_dict["sum__sum"], 2)
    except TypeError:
        invoices_sell_sum = 0

    year = current_year()
    now = now_date()
    q = request.GET.get("q", "")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

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

    template_path = "invoices/invoices_sell_pdf.html"

    context = {"invoices": invoicessell,"date_from": date_from,
               "date_to": date_to,"invoices_sell_sum": invoices_sell_sum, "now": now, "year": year,
               "invoices_sell_sum_dict": invoices_sell_sum_dict, "objects": objects,"user":user }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    now_time = now.strftime("%d-%m-%Y")
    response["Content-Disposition"] = "attachment; filename=Lista wystawionych faktur - utworzono {now_time}.pdf".format(now_time=now_time)
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html,  dest=response, encoding="UTF-8")
    # pisa_status = pisa.CreatePDF(html,  dest=response, encoding="UTF-8", path="'/main/static/fonts/arial.ttf'")

    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("Wystąpił jakiś problem :( Error:997 <pre>" + html + "</pre>")
    return response
