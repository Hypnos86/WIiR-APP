from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from contracts.models import ContractImmovables, AneksImmovables, ContractAuction, AneksContractAuction
from contracts.forms import ContractimmovablesForm, AneksForm, ContractAuctionForm


# Create your views here.
@login_required
def menu_contractsimmovables(request):
    contracts = ContractImmovables.objects.all().order_by("-data_umowy")
    query = "Wyczyść"
    search = "Szukaj"
    contrsum = len(contracts)
    q = request.GET.get("q")

    paginator = Paginator(contracts, 40)
    page_number = request.GET.get('page')
    contracts_list = paginator.get_page(page_number)

    if q:
        contracts = contracts.filter(kontrahent__nazwa__icontains=q)
        return render(request, 'contracts/contract_list.html',
                      {'contracts': contracts, "contrsum": contrsum, "query": query})
    else:
        return render(request, 'contracts/contract_list.html',
                      {'contracts': contracts_list, "contrsum": contrsum, "search": search})


@login_required
def new_contractsimmovables(request):
    contract_form = ContractimmovablesForm(request.POST or None, request.FILES or None)
    context = {'contract_form': contract_form,
               'new': True}

    if request.method == 'POST':
        if contract_form.is_valid():
            instance = contract_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('contracts:menu_contractsimmovables')

    return render(request, 'contracts/contract_form.html', context)


@login_required
def edit_contractsimmovables(request, id):
    contractsimmovables_edit = get_object_or_404(ContractImmovables, pk=id)
    contractsimmovables_form = ContractimmovablesForm(request.POST or None, request.FILES or None,
                                                      instance=contractsimmovables_edit)
    aneks_form = AneksForm(request.POST or None, request.FILES or None)

    context = {'contract_form': contractsimmovables_form,
               'aneks_form': aneks_form,
               'new': False}
    if contractsimmovables_form.is_valid():
        contract = contractsimmovables_form.save(commit=False)
        contract.author = request.user
        contractsimmovables_form.save()

        if aneks_form.is_valid():
            instance = aneks_form.save(commit=False)
            instance.autor = request.user
            instance.contractimmovables = contractsimmovables_edit
            instance.save()

        return redirect('contracts:menu_contractsimmovables')
    return render(request, 'contracts/contract_form.html', context)


@login_required
def show_contractsimmovables(request, id):
    contract = ContractImmovables.objects.get(pk=id)
    aneksy = contract.aneks.all()

    return render(request, 'contracts/show_contract_immovables.html', {'contract': contract, 'aneksy': aneksy})


@login_required
def new_aneks(request):
    aneks_form = AneksForm(request.POST or None, request.FILES or None)
    context = {'aneks_form': aneks_form,
               'new': True}

    if request.method == 'POST':
        if aneks_form.is_valid():
            instance = aneks_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('contracts:menu_contractsimmovables')

    return render(request, 'contracts/aneks_form.html', context)


@login_required
def menu_contracts_auction(request):
    contracts_auctions = ContractAuction.objects.all().order_by('-date')
    query = "Wyczyść"
    search = "Szukaj"
    contracts_auctions_sum = len(contracts_auctions)
    q = request.GET.get("q")

    paginator = Paginator(contracts_auctions, 20)
    page_number = request.GET.get('page')
    contracts_auctions_list = paginator.get_page(page_number)

    return render(request, 'contracts/contract_auction_list.html', {'contracts_auctions_list': contracts_auctions_list,
                                                                    'contracts_auctions_sum': contracts_auctions_sum})


@login_required
def new_contract_auction(request):
    contract_auction_form = ContractAuctionForm(request.POST or None, request.FILES or None)

    context = {'contract_auction_form': contract_auction_form,
               'new': True}

    if request.method == 'POST':
        if contract_auction_form.is_valid():
            instance = contract_auction_form.save(commit=False)
            instance.author = request.user
            instance.save()
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

    aneks_form = AneksContractAuction(request.POST or None, request.FILES or None)

    context = {'contract_auction_form': contract_auction_form,

               'new': False}

    if contract_auction_form.is_valid():
        contract = contract_auction_form.save(commit=False)
        contract.author = request.user
        contract_auction_form.save()

        return redirect('contracts:menu_contracts_auction')
    return render(request, 'contracts/contract_auction_form.html', context)
