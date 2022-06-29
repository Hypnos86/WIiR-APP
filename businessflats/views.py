from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from businessflats.models import OfficialFlat
from businessflats.forms import OfficialFlatForm
from django.core.paginator import Paginator


# Create your views here.
@login_required
def make_flats_list(request):
    flats = OfficialFlat.objects.all()
    count_flats = len(flats)

    paginator = Paginator(flats, 10)
    page_number = request.GET.get('page')
    flats_list = paginator.get_page(page_number)

    try:
        last_date = OfficialFlat.objects.values('change').latest('change')
    except OfficialFlat.DoesNotExist:
        last_date = None

    query = "Wyczyść"
    search = "Szukaj"
    q = request.GET.get("q")

    if q:
        flats = flats.filter(address__icontains=q) | flats.filter(area__startswith=q) | flats.filter(
            information__icontains=q)
        count_flats_query = len(flats)
        return render(request, 'businessflats/flats_list.html',
                      {'flats': flats, "query": query, 'last_date': last_date, 'count_flats': count_flats_query})
    else:
        return render(request, 'businessflats/flats_list.html',
                      {'flats': flats_list, "search": search,
                       'last_date': last_date, 'count_flats': count_flats})


@login_required
def show_information(request, id):
    flat = get_object_or_404(OfficialFlat, pk=id)
    return render(request, 'businessflats/information_popup.html', {'flat': flat, 'id': id})


@login_required
def add_new_flat(request):
    new_flat_form = OfficialFlatForm(request.POST or None)

    if request.method == 'POST':
        if new_flat_form.is_valid():
            instance = new_flat_form.save(commit=False)
            instance.author = request.user
            instance.save()
            new_flat_form.save()
            return redirect('businessflats:make_flats_list')
    return render(request, 'businessflats/flat_form.html', {'flat_form': new_flat_form, 'new': True})


@login_required
def edit_flat(request, id):
    flats = get_object_or_404(OfficialFlat, pk=id)
    flat_form = OfficialFlatForm(request.POST or None, instance=flats)
    context = {'flat_form': flat_form, 'new': False}

    if request.method == 'POST':
        if flat_form.is_valid():
            flat = flat_form.save(commit=False)
            flat.author = request.user
            flat_form.save()
            return redirect('businessflats:make_flats_list')
    return render(request, 'businessflats/flat_form.html', context)
