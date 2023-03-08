from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from businessflats.models import OfficialFlat
from businessflats.forms import OfficialFlatForm
from django.core.paginator import Paginator


# Create your views here.
# @login_required
# def make_flats_list(request):
#     flats = OfficialFlat.objects.all().order_by('address')
#     count_flats = len(flats)
#
#     paginator = Paginator(flats, 10)
#     page_number = request.GET.get('page')
#     flats_list = paginator.get_page(page_number)
#
#     try:
#         last_date = OfficialFlat.objects.values('change').latest('change')
#     except OfficialFlat.DoesNotExist:
#         last_date = None
#
#     query = "Wyczyść"
#     search = "Szukaj"
#     q = request.GET.get("q")
#
#     if q:
#         flats = flats.filter(address__icontains=q) | flats.filter(area__startswith=q) | flats.filter(
#             information__icontains=q)
#         count_flats_query = len(flats)
#         return render(request, 'businessflats/flats_list.html',
#                       {'flats': flats, "query": query, 'last_date': last_date, 'count_flats': count_flats_query})
#     else:
#         return render(request, 'businessflats/flats_list.html',
#                       {'flats': flats_list, "search": search,
#                        'last_date': last_date, 'count_flats': count_flats})

class MakeFlatsListView(LoginRequiredMixin, View):
    template_name = 'businessflats/flats_list.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        flats = OfficialFlat.objects.all().order_by('address')
        count_flats = len(flats)

        paginator = Paginator(flats, self.paginate_by)
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
            context = {'flats': flats, "query": query, 'last_date': last_date, 'count_flats': count_flats_query}
        else:
            context = {'flats': flats_list, "search": search,
                       'last_date': last_date, 'count_flats': count_flats}

        return render(request, self.template_name, context)

# @login_required
# def show_information(request, id):
#     """
#
#     Parameters
#     ----------
#     request
#     id - klucz obiektu OfficjalFlat
#
#     Returns
#     -------
#     Zwraca informacje dla obiektu
#     """
#     flat = get_object_or_404(OfficialFlat, pk=id)
#     return render(request, 'businessflats/info_flat_popup.html', {'flat': flat, 'id': id})
class ShowInformationView(LoginRequiredMixin, View):
    template_name = 'businessflats/info_flat_popup.html'

    def get(self, request, id, *args, **kwargs):
        flat = get_object_or_404(OfficialFlat, pk=id)
        context = {'flat': flat, 'id': id}
        return render(request, self.template_name, context)

# @login_required
# def add_new_flat(request):
#     """
#
#     Parameters
#     ----------
#     request
#
#     Returns
#     -------
#     Zapisuje nowy obiekt w bazie
#     """
#     new_flat_form = OfficialFlatForm(request.POST or None)
#
#     if request.method == 'POST':
#         if new_flat_form.is_valid():
#             instance = new_flat_form.save(commit=False)
#             instance.author = request.user
#             new_flat_form.save()
#             return redirect('businessflats:make_flats_list')
#     return render(request, 'businessflats/flat_form.html', {'flat_form': new_flat_form, 'new': True})

class AddNewFlatView(LoginRequiredMixin, View):
    template_name = 'businessflats/flat_form.html'
    form_class = OfficialFlatForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'flat_form': form, 'new': True}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            return redirect('businessflats:make_flats_list')
        context = {'flat_form': form, 'new': True}
        return render(request, self.template_name, context)

# @login_required
# def edit_flat(request, id):
#     """
#
#     Parameters
#     ----------
#     request
#     id - klucz obiektu OfficjalFlat
#
#     Returns
#     -------
#     Edytuje obiekt w bazie
#     """
#     flats = get_object_or_404(OfficialFlat, pk=id)
#     flat_form = OfficialFlatForm(request.POST or None, instance=flats)
#     context = {'flat_form': flat_form, 'new': False}
#
#     if request.method == 'POST':
#         if flat_form.is_valid():
#             flat = flat_form.save(commit=False)
#             flat.author = request.user
#             flat_form.save()
#             return redirect('businessflats:make_flats_list')
#     return render(request, 'businessflats/flat_form.html', context)

class EditFlatView(LoginRequiredMixin, View):
    template_name = 'businessflats/flat_form.html'
    form_class = OfficialFlatForm

    def get(self, request, id, *args, **kwargs):
        flat = get_object_or_404(OfficialFlat, pk=id)
        form = self.form_class(instance=flat)
        context = {'flat_form': form, 'new': False}
        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        flat = get_object_or_404(OfficialFlat, pk=id)
        form = self.form_class(request.POST or None, instance=flat)
        if form.is_valid():
            flat = form.save(commit=False)
            flat.author = request.user
            form.save()
            return redirect('businessflats:make_flats_list')
        context = {'flat_form': form, 'new': False}
        return render(request, self.template_name, context)