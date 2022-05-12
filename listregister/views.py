from django.shortcuts import render, redirect, get_object_or_404
from listregister.models import OfficialFlat
from listregister.forms import OfficialFlatForm


# Create your views here.
def make_list_register(request):
    flats = OfficialFlat.objects.all()
    count_flats = len(flats)
    context = {'count_flats': count_flats}
    return render(request, 'list_register.html', context)


def make_flats_list(request):
    flats = OfficialFlat.objects.all()
    last_date = OfficialFlat.objects.values('change').latest('change')
    count_flats = len(flats)
    query = "Wyczyść"
    search = "Szukaj"
    q = request.GET.get("q")

    if q:
        flats = flats.filter(address__icontains=q) | flats.filter(area__startswith=q) | flats.filter(
            information__icontains=q)
        return render(request, 'listregister/flats_list.html',
                      {'flats': flats, "query": query, 'last_date': last_date, 'count_flats': count_flats})
    else:
        return render(request, 'listregister/flats_list.html',
                      {'flats': flats, "search": search,
                       'last_date': last_date, 'count_flats': count_flats})


def add_new_flat(request):
    new_flat_form = OfficialFlatForm(request.POST or None)

    if request.method == 'POST':
        if new_flat_form.is_valid():
            instance = new_flat_form.save(commit=False)
            instance.author = request.user
            instance.save()
            new_flat_form.save()
            return redirect('listregister:make_flats_list')
    return render(request, 'listregister/flat_form.html', {'flat_form': new_flat_form, 'new': True})


def edit_flat(request, id):
    flats = get_object_or_404(OfficialFlat, pk=id)
    flat_form = OfficialFlatForm(request.POST or None, instance=flats)
    context = {'flat_form': flat_form, 'new': False}

    if request.method == 'POST':
        if flat_form.is_valid():
            flat = flat_form.save(commit=False)
            flat.author = request.user
            flat_form.save()
            return redirect('listregister:make_flats_list')
    return render(request, 'listregister/flat_form.html', context)