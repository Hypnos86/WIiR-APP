from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views import View

from contracts.models import ContractImmovables, ContractAuction, AnnexContractAuction, ContractMedia, \
    GuaranteeSettlement, FinancialDocument
from contracts.forms import ContractImmovablesForm, ContractAuctionForm, AnnexImmovablesForm, AnnexContractAuctionForm, \
    ContractMediaForm, AnnexContractMediaForm, GuaranteeSettlementForm, FinancialDocumentForm
from main.models import AccessModule
from django.contrib.auth.models import User
from units.models import Unit
from main.models import Employer
from main.views import now_date
from decimal import Decimal
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from main.models import TeamEnum


# Create your views here.
class ContractsImmovableListView(LoginRequiredMixin, View):
    template = "contracts/list_immovable.html"

    def get(self, request):
        contracts = ContractImmovables.objects.all().order_by("-date").filter(state=True)
        contracts_archive = ContractImmovables.objects.all().order_by("-date").filter(state=False)
        now = now_date

        try:
            last_date = ContractImmovables.objects.values('change').latest('change')
        except ContractImmovables.DoesNotExist:
            last_date = None

        query = "Wyczyść"
        search = "Szukaj"
        con_len = len(contracts)
        con_archive_sum = len(contracts_archive)
        q = request.GET.get("q")
        date_from = request.GET.get('from')
        date_to = request.GET.get('to')

        paginator = Paginator(contracts, 50)
        page_number = request.GET.get('page')
        contracts_list = paginator.get_page(page_number)
        if q or date_from or date_to:
            if q:
                contracts = contracts.filter(contractor__name__icontains=q) | contracts.filter(
                    type_of_contract__type__icontains=q) | contracts.filter(
                    unit__county__name__icontains=q) | contracts.filter(
                    unit__city__icontains=q)

            if date_from:
                contracts = contracts.filter(date__gte=date_from)

            if date_to:
                contracts = contracts.filter(date__lte=date_to)
            context = {'contracts': contracts, 'con_archive_sum': con_archive_sum, 'con_len': con_len,
                       'query': query, 'last_date': last_date, 'now': now, 'q': q, 'date_from': date_from,
                       'date_to': date_to, 'actual': True}
            return render(request, self.template, context)
        else:
            context = {'contracts': contracts_list, 'con_len': con_len, 'con_archive_sum': con_archive_sum,
                       'search': search, 'last_date': last_date, 'now': now, 'actual': True}
            return render(request, 'contracts/list_immovable.html', context)


class ContractsArchiveImmovableListView(LoginRequiredMixin, View):
    template = "contracts/list_immovable.html"

    def get(self, request):
        contracts = ContractImmovables.objects.all().order_by("-date").filter(state=True)
        contracts_archive = ContractImmovables.objects.all().order_by("-date").filter(state=False)

        query = "Wyczyść"
        search = "Szukaj"
        con_len = len(contracts)
        con_archive_sum = len(contracts_archive)
        q = request.GET.get("q")
        date_from = request.GET.get('from')
        date_to = request.GET.get('to')

        paginator = Paginator(contracts_archive, 50)
        page_number = request.GET.get('page')
        contracts_list = paginator.get_page(page_number)
        if q or date_from or date_to:
            if q:
                contracts = contracts_archive.filter(contractor__name__icontains=q)

            if date_from:
                contracts = contracts_archive.filter(date__gte=date_from)

            if date_to:
                contracts = contracts_archive.filter(date__lte=date_to)

            context = {'contracts_archive': contracts, 'con_archive_sum': con_archive_sum, 'con_len': con_len,
                       'query': query, 'q': q, 'date_from': date_from, 'date_to': date_to, 'actual': False}
            return render(request, self.template, context)
        else:
            context = {'contracts_archive': contracts_list, 'con_len': con_len, 'con_archive_sum': con_archive_sum,
                       'search': search, 'actual': False}
            return render(request, 'contracts/list_immovable.html', context)


@login_required
def new_contractsimmovables(request):
    contract_form = ContractImmovablesForm(request.POST or None, request.FILES or None)
    units = Unit.objects.all().order_by("county__id_order")
    context = {'contract_form': contract_form,
               'units': units,
               'new': True}

    if request.method == 'POST':
        if contract_form.is_valid():
            instance = contract_form.save(commit=False)
            instance.author = request.user
            contract_form.save()
            return redirect('contracts:menu_contractsimmovables')

    return render(request, 'contracts/contract_form.html', context)


@login_required
def edit_contractsimmovables(request, id):
    contractsimmovables_edit = get_object_or_404(ContractImmovables, pk=id)
    contractsimmovables_form = ContractImmovablesForm(request.POST or None, request.FILES or None,
                                                      instance=contractsimmovables_edit)

    units = Unit.objects.all().order_by("county__id_order")
    unit_edit = contractsimmovables_edit

    context = {'contract_form': contractsimmovables_form,
               'units': units,
               'contract': contractsimmovables_edit,
               'unit_edit': unit_edit,
               'new': False}
    if request.method == 'POST':
        if contractsimmovables_form.is_valid():
            contract = contractsimmovables_form.save(commit=False)
            contract.author = request.user
            contractsimmovables_form.save()
            return redirect('contracts:menu_contractsimmovables')
    return render(request, 'contracts/contract_form.html', context)


@login_required
def add_annex_immovables(request, id):
    contractsimmovables_edit = get_object_or_404(ContractImmovables, pk=id)
    add_annex_form = AnnexImmovablesForm(request.POST or None, request.FILES or None)
    context = {'annex_form': add_annex_form,
               'contract_id': id}

    if request.method == 'POST':
        if add_annex_form.is_valid():
            instance = add_annex_form.save(commit=False)
            instance.author = request.user
            instance.contract_immovables = contractsimmovables_edit
            add_annex_form.save()

        return redirect('contracts:menu_contractsimmovables')

    if request.method == 'GET':
        return render(request, 'contracts/new_annex_immovables_form.html', context)


class ShowContractImmovableView(LoginRequiredMixin, View):
    template = "contracts/show_contract_immovable.html"

    def get(self, request, id):
        contract = ContractImmovables.objects.get(pk=id)
        annexes = contract.annex.all()
        context = {'contract': contract, 'annexes': annexes, 'actual': True}
        return render(request, self.template, context)


class ContractsAuctionListView(LoginRequiredMixin, View):
    template = "contracts/list_contract_auction.html"

    def get(self, request):
        contracts_auctions = ContractAuction.objects.all().order_by('-date')
        contracts_auctions_sum = len(contracts_auctions)
        query = "Wyczyść"
        search = "Szukaj"

        paginator = Paginator(contracts_auctions, 20)
        page_number = request.GET.get('page')
        contracts_auctions_list = paginator.get_page(page_number)

        q = request.GET.get("q")
        date_from = request.GET.get('from')
        date_to = request.GET.get('to')

        try:
            last_date = ContractAuction.objects.values('change').latest('change')
        except ContractAuction.DoesNotExist:
            last_date = None

        if q or date_from or date_to:
            if q:
                contracts_auctions = contracts_auctions.filter(no_contract__icontains=q) \
                                     | contracts_auctions.filter(contractor__name__icontains=q) \
                                     | contracts_auctions.filter(unit__county__name__icontains=q) \
                                     | contracts_auctions.filter(unit__city__icontains=q) \
                                     | contracts_auctions.filter(unit__address__icontains=q) \
                                     | contracts_auctions.filter(work_scope__icontains=q) \
                                     | contracts_auctions.filter(worker__name__icontains=q) \
                                     | contracts_auctions.filter(worker__last_name__icontains=q)

            if date_from:
                contracts_auctions = contracts_auctions.filter(date__gte=date_from)

            if date_to:
                contracts_auctions = contracts_auctions.filter(date__lte=date_to)

            contracts_auctions_sum = len(contracts_auctions)
            context = {'contracts_auctions_list': contracts_auctions,
                       'contracts_auctions_sum': contracts_auctions_sum, 'last_date': last_date, 'query': query,
                       'q': q, 'date_from': date_from, 'date_to': date_to}
            return render(request, self.template, context)

        else:
            context = {'contracts_auctions_list': contracts_auctions_list,
                       'contracts_auctions_sum': contracts_auctions_sum, 'last_date': last_date, 'search': search}
            return render(request, self.template, context)


@login_required
def new_contract_auction(request):
    contract_auction_form = ContractAuctionForm(request.POST or None, request.FILES or None)
    contract_auction_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all().order_by("county__id_order")
    context = {'contract_auction_form': contract_auction_form,
               'units': units,
               'new': True}

    if request.method == 'POST':
        if contract_auction_form.is_valid():
            instance = contract_auction_form.save(commit=False)
            instance.author = request.user
            contract_auction_form.save()
            return redirect('contracts:menu_contracts_auction')
    return render(request, 'contracts/contract_auction_form.html', context)


class ShowContractAuctionView(LoginRequiredMixin, View):
    template = "contracts/show_contract_auction.html"

    def get(self, request, id):
        contract = ContractAuction.objects.get(pk=id)
        annexes = contract.aneks_contract_auction.all()
        context = {'contract': contract,
                   'annexes': annexes}
        return render(request, self.template, context)


@login_required
def edit_contract_auction(request, id):
    contract_auction_edit = get_object_or_404(ContractAuction, pk=id)
    contract_auction_form = ContractAuctionForm(request.POST or None, request.FILES or None,
                                                instance=contract_auction_edit)
    contract_auction_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all().order_by("county__id_order")
    unit_edit = contract_auction_edit

    context = {'contract_auction_form': contract_auction_form,
               'units': units,
               'contract': contract_auction_edit,
               'unit_edit': unit_edit,
               'new': False}

    if request.method == 'POST':
        if contract_auction_form.is_valid():
            contract = contract_auction_form.save(commit=False)
            contract.author = request.user
            contract_auction_form.save()
            try:
                days_30 = timedelta(days=30)
                sum_30_percent = contract.security_sum * 30 * Decimal(0.01)
                settlement_30_day = contract.last_report_date + days_30

                months = contract.warranty_period
                sum_70_percent = contract.security_sum * 70 * Decimal(0.01)
                settlement_warranty_period = contract.last_report_date + relativedelta(months=months)

                settlement_period = [settlement_30_day, settlement_warranty_period]
                settlement_sum = [sum_30_percent, sum_70_percent]

                settlements = zip(settlement_period, settlement_sum)

                if contract.last_report_date != 0:
                    print('pierwszy if')
                    print(f'{contract.id}')
                    print(f"{list(GuaranteeSettlement.objects.all().values_list('contract', flat=True))}")
                    if contract.id in list(GuaranteeSettlement.objects.all().values_list('contract', flat=True)):
                        print('drugi if')
                        if contract.guarantee.id == 2:
                            print('trzeci if')
                            settlement_guarantee = GuaranteeSettlement.objects.filter(contract=contract_auction_edit)
                            settlement_guarantee.delete()
                            for date, sum in settlements:
                                print("for 3 if1")
                                settlement_guarantee = GuaranteeSettlement.objects.create(
                                    contract=contract_auction_edit, deadline_settlement=date, settlement_sum=sum)

                        else:
                            print(f'3 if bez fora1 - {contract.security_sum}')
                            settlement_guarantee = GuaranteeSettlement.objects.filter(contract=contract_auction_edit)
                            settlement_guarantee.delete()
                            settlement_guarantee = GuaranteeSettlement.objects.create(contract=contract_auction_edit,
                                                                                      deadline_settlement=settlement_30_day,
                                                                                      settlement_sum=contract.security_sum)

                        return redirect('contracts:menu_contracts_auction')
                    else:
                        if contract.guarantee.id == 2:
                            print('trzeci if2')
                            for date, sum in settlements:
                                settlement_guarantee = GuaranteeSettlement.objects.create(
                                    contract=contract_auction_edit,
                                    deadline_settlement=date,
                                    settlement_sum=sum)
                                print("for 4 if")

                        else:

                            settlement_guarantee = GuaranteeSettlement.objects.create(contract=contract_auction_edit,
                                                                                      deadline_settlement=settlement_30_day,
                                                                                      settlement_sum=contract.security_sum)
                            print('4 if bez fora2')

                        return redirect('contracts:menu_contracts_auction')

            except TypeError:
                return redirect('contracts:menu_contracts_auction')

    return render(request, 'contracts/contract_auction_form.html', context)


@login_required
def add_annex_contract_auction(request, id):
    contract_edit = get_object_or_404(ContractAuction, pk=id)
    add_annex_form = AnnexContractAuctionForm(request.POST or None, request.FILES or None)
    context = {'annex_form': add_annex_form,
               'contract_id': id}

    if request.method == 'POST':
        if add_annex_form.is_valid():
            instance = add_annex_form.save(commit=False)
            instance.author = request.user
            instance.contract_auction = contract_edit
            add_annex_form.save()
            return redirect('contracts:menu_contracts_auction')
    if request.method == 'GET':
        return render(request, 'contracts/new_annex_auction_form.html', context)


@login_required
def new_contract_media(request):
    contract_form = ContractMediaForm(request.POST or None, request.FILES or None)
    contract_form.fields['employer'].queryset = Employer.objects.all().filter(industry_specialist=True).filter(
        team__team='Zespół Eksploatacji')
    contract_form.fields['unit'].queryset = Unit.objects.all().order_by("county__id_order")
    units = Unit.objects.all()

    if request.method == 'POST':
        if contract_form.is_valid():
            instance = contract_form.save(commit=False)
            instance.author = request.user
            contract_form.save()
            return redirect('contracts:create_contract_media_list')
    return render(request, 'contracts/contract_media_form.html',
                  {'contract_form': contract_form, 'new': True, 'units': units})


@login_required
def edit_contract_media(request, id):
    contract_edit = get_object_or_404(ContractMedia, pk=id)
    contract_form = ContractMediaForm(request.POST or None, request.FILES or None, instance=contract_edit)
    contract_form.fields['employer'].queryset = Employer.objects.all().filter(team__id=TeamEnum.ZE.value[0])
    contract_form.fields['unit'].queryset = Unit.objects.all().order_by('county')

    units = Unit.objects.all()
    selected_units = contract_edit.unit.all()

    if request.method == 'POST':
        if contract_form.is_valid():
            instance = contract_form.save(commit=False)
            instance.author = request.user
            contract_form.save()
            return redirect('contracts:create_contract_media_list')
    return render(request, 'contracts/contract_media_form.html',
                  {'contract_form': contract_form, 'new': False, 'units': units, 'contract_edit': contract_edit,
                   'selected_units': selected_units, "back_to_show_info": True, "id": id})


class ContractMediaListView(LoginRequiredMixin, View):
    template = "contracts/list_contracts_media.html"

    def get(self, request):
        contracts_media = ContractMedia.objects.all().filter(state=True).order_by('-date').distinct()
        contracts_media_len = len(contracts_media)
        now = now_date
        query = "Wyczyść"
        search = "Szukaj"

        paginator = Paginator(contracts_media, 50)
        page_number = request.GET.get('page')
        contracts_media_list = paginator.get_page(page_number)

        q = request.GET.get("q")
        date_from = request.GET.get('from')
        date_to = request.GET.get('to')

        try:
            last_date = ContractMedia.objects.values('change').latest('change')
        except ContractMedia.DoesNotExist:
            last_date = None

        if q or date_from or date_to:
            if q:
                contracts_media = contracts_media.filter(no_contract__icontains=q) \
                                  | contracts_media.filter(type__type__icontains=q) \
                                  | contracts_media.filter(contractor__name__icontains=q) \
                                  | contracts_media.filter(unit__city__icontains=q) \
                                  | contracts_media.filter(unit__type__type_short__icontains=q) \
                                  | contracts_media.filter(employer__name__icontains=q) \
                                  | contracts_media.filter(employer__last_name__icontains=q) \
                                  | contracts_media.filter(content__icontains=q)

            if date_from:
                contracts_media = contracts_media.filter(date__gte=date_from)

            if date_to:
                contracts_media = contracts_media.filter(date__lte=date_to)

            contracts_media_len = len(contracts_media)
            context = {'actual': True, 'contracts_media': contracts_media,
                       'contracts_media_len': contracts_media_len,
                       'q': q, 'date_from': date_from, 'date_to': date_to, 'last_date': last_date, 'query': query,
                       'now': now}
            return render(request, self.template, context
                          )
        else:
            context = {'contracts_media': contracts_media_list,
                       'contracts_media_len': contracts_media_len, 'last_date': last_date, 'search': search,
                       'actual': True, 'now': now}
            return render(request, self.template, context)


class ContractsArchiveMediaListView(LoginRequiredMixin, View):
    template = "contracts/list_contracts_media.html"

    def get(self, request):
        contracts_media = ContractMedia.objects.all().filter(state=False).order_by('-date').distinct()
        contracts_media_len = len(contracts_media)
        now = now_date
        query = "Wyczyść"
        search = "Szukaj"

        paginator = Paginator(contracts_media, 50)
        page_number = request.GET.get('page')
        contracts_media_list = paginator.get_page(page_number)

        q = request.GET.get("q")
        date_from = request.GET.get('from')
        date_to = request.GET.get('to')

        try:
            last_date = ContractMedia.objects.values('change').latest('change')
        except ContractMedia.DoesNotExist:
            last_date = None

        if q or date_from or date_to:
            if q:
                contracts_media = contracts_media.filter(no_contract__icontains=q) \
                                  | contracts_media.filter(type__type__icontains=q) \
                                  | contracts_media.filter(contractor__name__icontains=q) \
                                  | contracts_media.filter(unit__city__icontains=q) \
                                  | contracts_media.filter(unit__type__type_short__icontains=q) \
                                  | contracts_media.filter(employer__name__icontains=q) \
                                  | contracts_media.filter(employer__last_name__icontains=q) \
                                  | contracts_media.filter(content__icontains=q)

            if date_from:
                contracts_media = contracts_media.filter(date__gte=date_from)

            if date_to:
                contracts_media = contracts_media.filter(date__lte=date_to)

            contracts_media_len = len(contracts_media)
            context = {'actual': False, 'contracts_media': contracts_media,
                       'contracts_media_len': contracts_media_len,
                       'q': q, 'date_from': date_from, 'date_to': date_to, 'last_date': last_date, 'query': query,
                       'now': now}
            return render(request, self.template, context)
        else:
            context = {'contracts_media': contracts_media_list,
                       'contracts_media_len': contracts_media_len, 'last_date': last_date, 'search': search,
                       'actual': False, 'now': now}
            return render(request, self.template, context)


@login_required
def show_contract_media(request, id):
    contract_media = ContractMedia.objects.get(pk=id)
    units = contract_media.unit.all()
    annexes = contract_media.annex_contract_media.all()
    return render(request, 'contracts/show_contract_media.html',
                  {'contract': contract_media, 'annexes': annexes, 'units': units, "id": id})


@login_required
def add_annex_contract_media(request, id):
    contract_edit = get_object_or_404(ContractMedia, pk=id)
    add_annex_form = AnnexContractMediaForm(request.POST or None, request.FILES or None)

    context = {'annex_form': add_annex_form,
               'contract_id': id}

    if request.method == 'POST':
        if add_annex_form.is_valid():
            instance = add_annex_form.save(commit=False)
            instance.author = request.user
            instance.contract_media = contract_edit
            add_annex_form.save()
            return redirect('contracts:create_contract_media_list')
    if request.method == 'GET':
        return render(request, 'contracts/new_annex_media_form.html', context)


@login_required
def edit_settlement(request, id):
    settlement_model = get_object_or_404(GuaranteeSettlement, pk=id)
    settlement_form = GuaranteeSettlementForm(request.POST or None, instance=settlement_model)

    if request.method == "POST":
        if settlement_form.is_valid():
            instance = settlement_form.save(commit=False)
            instance.settlement_sum = settlement_model.settlement_sum
            instance.deadline_settlement = settlement_model.deadline_settlement
            instance.save()
        return redirect("investments:make_important_task_investments")

    return render(request, "contracts/settlement_form.html",
                  {"settlement_form": settlement_form, "settlement_model": settlement_model, "id": id})


@login_required
def show_information_settlement(request, id):
    settlement = get_object_or_404(GuaranteeSettlement, pk=id)
    return render(request, "contracts/settlement_popup.html", {"settlement": settlement, "id": id})


@login_required
def financial_document_list(request, contract_id):
    contract = get_object_or_404(ContractMedia, pk=contract_id)
    financialDocs = FinancialDocument.objects.all().filter(contract__id=contract.id)

    sum_count = 0
    values_sum = []
    costs_sum = []

    for docs in financialDocs:
        sum_count += docs.value
        values_sum.append(docs.value)
        costs_sum.append(docs.cost_brutto)

    values = sum(values_sum)
    costs = sum(costs_sum)
    context = {"contract": contract, "financialDocs": financialDocs, "values": values, "costs": costs}
    return render(request, "contracts/financial_document_list.html", context)


@login_required
def add_financial_document(request, contract_id):
    contract = get_object_or_404(ContractMedia, pk=contract_id)
    add_document_form = FinancialDocumentForm(request.POST or None)

    if request.method == 'POST':
        if add_document_form.is_valid():
            instance = add_document_form.save(commit=False)
            instance.contract = contract
            instance.author = request.user
            add_document_form.save()
            return redirect(reverse('contracts:financial_document_list', kwargs={"contract_id": contract_id}))
    return render(request, 'contracts/financial_media_form.html',
                  {'document': add_document_form, 'contract_id': contract_id, 'new': True})


@login_required
def edit_financial_document(request, contract_id, id):
    contract = get_object_or_404(ContractMedia, pk=contract_id)
    edit_document = get_object_or_404(FinancialDocument, pk=id)
    add_document_form = FinancialDocumentForm(request.POST or None, instance=edit_document)

    if request.method == 'POST':
        if add_document_form.is_valid():
            instance = add_document_form.save(commit=False)
            instance.contract = contract
            instance.author = request.user
            add_document_form.save()
            return redirect(reverse('contracts:financial_document_list', kwargs={"contract_id": contract_id}))
    return render(request, 'contracts/financial_media_form.html',
                  {'document': add_document_form, 'contract_id': contract_id, 'new': False})
