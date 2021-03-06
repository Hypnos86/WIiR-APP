from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from contracts.models import ContractImmovables, ContractAuction, AnnexContractAuction, ContractMedia
from contracts.forms import ContractImmovablesForm, ContractAuctionForm, AnnexImmovablesForm, AnnexContractAuctionForm, \
    ContractMediaForm
from units.models import Unit
from main.models import Employer
from main.views import now_date


# Create your views here.
@login_required
def menu_contractsimmovables(request):
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

    paginator = Paginator(contracts, 50)
    page_number = request.GET.get('page')
    contracts_list = paginator.get_page(page_number)
    # print(contracts.period_of_validity)
    if q:
        contracts = contracts.filter(contractor__name__icontains=q) | contracts.filter(
            type_of_contract__type__icontains=q) | contracts.filter(unit__county__name__icontains=q) | contracts.filter(
            unit__city__icontains=q)
        return render(request, 'contracts/contract_list.html',
                      {'contracts': contracts, 'con_archive_sum': con_archive_sum, 'con_len': con_len,
                       'query': query, 'last_date': last_date, 'now': now, 'actual': True})
    else:
        return render(request, 'contracts/contract_list.html',
                      {'contracts': contracts_list, 'con_len': con_len, 'con_archive_sum': con_archive_sum,
                       'search': search, 'last_date': last_date, 'now': now, 'actual': True})


@login_required
def menu_contractsimmovables_archive(request):
    contracts = ContractImmovables.objects.all().order_by("-date").filter(state=True)
    contracts_archive = ContractImmovables.objects.all().order_by("-date").filter(state=False)

    query = "Wyczyść"
    search = "Szukaj"
    contrsum = len(contracts)
    con_archive_sum = len(contracts_archive)
    q = request.GET.get("q")

    paginator = Paginator(contracts_archive, 50)
    page_number = request.GET.get('page')
    contracts_list = paginator.get_page(page_number)

    if q:
        contracts = contracts_archive.filter(contractor__name__icontains=q)
        return render(request, 'contracts/contract_list.html',
                      {'contracts_archive': contracts, 'con_archive_sum': con_archive_sum, 'contrsum': contrsum,
                       'query': query, 'actual': False})
    else:
        return render(request, 'contracts/contract_list.html',
                      {'contracts_archive': contracts_list, 'contrsum': contrsum, 'con_archive_sum': con_archive_sum,
                       'search': search, 'actual': False})


@login_required
def new_contractsimmovables(request):
    contract_form = ContractImmovablesForm(request.POST or None, request.FILES or None)
    units = Unit.objects.all()
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

    units = Unit.objects.all()
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


@login_required
def show_contractsimmovables(request, id):
    contract = ContractImmovables.objects.get(pk=id)
    annexes = contract.annex.all()

    return render(request, 'contracts/show_contract_immovables.html',
                  {'contract': contract, 'annexes': annexes, 'actual': True})


@login_required
def menu_contracts_auction(request):
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
                                 | contracts_auctions.filter(work_scope__icontains=q) \
                                 | contracts_auctions.filter(worker__name__icontains=q) \
                                 | contracts_auctions.filter(worker__last_name__icontains=q)

        if date_from:
            contracts_auctions = contracts_auctions.filter(date__gte=date_from)

        if date_to:
            contracts_auctions = contracts_auctions.filter(date__lte=date_to)

        contracts_auctions_sum = len(contracts_auctions)

        return render(request, 'contracts/contract_auction_list.html',
                      {'contracts_auctions_list': contracts_auctions,
                       'contracts_auctions_sum': contracts_auctions_sum, 'last_date': last_date, 'query': query,
                       'q': q, 'date_from': date_from, 'date_to': date_to})

    else:
        return render(request, 'contracts/contract_auction_list.html',
                      {'contracts_auctions_list': contracts_auctions_list,
                       'contracts_auctions_sum': contracts_auctions_sum, 'last_date': last_date, 'search': search})


@login_required
def new_contract_auction(request):
    contract_auction_form = ContractAuctionForm(request.POST or None, request.FILES or None)
    contract_auction_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all()
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


@login_required
def show_contract_auction(request, id):
    contract = ContractAuction.objects.get(pk=id)
    annexes = contract.aneks_contract_auction.all()
    context = {'contract': contract,
               'annexes': annexes}
    return render(request, 'contracts/show_contract_auction.html', context)


@login_required
def edit_contract_auction(request, id):
    contract_auction_edit = get_object_or_404(ContractAuction, pk=id)
    contract_auction_form = ContractAuctionForm(request.POST or None, request.FILES or None,
                                                instance=contract_auction_edit)
    contract_auction_form.fields['worker'].queryset = Employer.objects.all().filter(industry_specialist=True)
    units = Unit.objects.all()
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
            contract_edit.save()

        return redirect('contracts:menu_contracts_auction')

    if request.method == 'GET':
        return render(request, 'contracts/new_annex_auction_form.html', context)


@login_required
def new_contract_media(request):
    contract_form = ContractMediaForm(request.POST or None, request.FILES or None)
    contract_form.fields['employer'].queryset = Employer.objects.all().filter(industry_specialist=True).filter(
        team__team='Zespół Ekploatacji')
    contract_form.fields['unit'].queryset = Unit.objects.all().order_by('county')
    units = Unit.objects.all()

    if request.method == 'POST':
        if contract_form.is_valid():
            instance = contract_form.save(commit=False)
            instance.author = request.user
            return redirect('contracts:create_contract_media_list')

    return render(request, 'contracts/contract_media_form.html',
                  {'contract_form': contract_form, 'new': True, 'units': units})


@login_required
def create_contract_media_list(request):
    contracts_media = ContractMedia.objects.all().filter(state=True).order_by('-date')
    contracts_media_len = len(contracts_media)
    query = "Wyczyść"
    search = "Szukaj"

    paginator = Paginator(contracts_media, 50)
    page_number = request.GET.get('page')
    contracts_media_list = paginator.get_page(page_number)

    q = request.GET.get("q")
    date_from = request.GET.get('from')
    date_to = request.GET.get('to')

    try:
        last_date = ContractMedia.objects.values('change_date').latest('change_date')
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
                              | contracts_media.filter(employer__last_name__icontains=q)

        if date_from:
            contracts_media = contracts_media.filter(date__gte=date_from)

        if date_to:
            contracts_media = contracts_media.filter(date__lte=date_to)

        contracts_media_len = len(contracts_media)

        return render(request, 'contracts/contracts_media_list.html',
                      {'actual': True, 'contracts_media': contracts_media, 'contracts_media_len': contracts_media_len,
                       'q': q, 'date_from': date_from, 'date_to': date_to, 'last_date': last_date, 'query': query})
    else:
        return render(request, 'contracts/contracts_media_list.html',
                      {'contracts_media': contracts_media_list,
                       'contracts_media_len': contracts_media_len, 'last_date': last_date, 'search': search})
