from django.shortcuts import render, redirect
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
    count_flats = len(flats)
    context = {'flats': flats, 'count_flats': count_flats}
    return render(request, 'listregister/flats_list.html', context)


def add_new_flat(request):
    new_flat_form = OfficialFlatForm(request.POST or None)

    if request.method == 'POST':
        if new_flat_form.is_valid():
            instance = new_flat_form.save(commit=False)
            instance.author = request.user
            instance.save()
            new_flat_form.save()
            return redirect('listregister:make_flats_list')
    return render(request, 'listregister/add_new_flat.html', {'new_flat_form': new_flat_form, 'new': True})
