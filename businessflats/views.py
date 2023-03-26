from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from businessflats.models import OfficialFlat
from businessflats.forms import OfficialFlatForm
from django.core.paginator import Paginator


class FlatsListView(LoginRequiredMixin, View):
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
            flats = flats.filter(address__icontains=q) \
                    | flats.filter(area__startswith=q) \
                    | flats.filter(information__icontains=q) \
                    | flats.filter(city__icontains=q)
            count_flats_query = len(flats)
            context = {'flats': flats, "query": query, 'last_date': last_date, 'count_flats': count_flats_query}
        else:
            context = {'flats': flats_list, "search": search,
                       'last_date': last_date, 'count_flats': count_flats}

        return render(request, self.template_name, context)


class ShowInformationView(LoginRequiredMixin, View):
    template_name = 'businessflats/info_flat_popup.html'

    def get(self, request, id, *args, **kwargs):
        flat = get_object_or_404(OfficialFlat, pk=id)
        context = {'flat': flat, 'id': id}
        return render(request, self.template_name, context)


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
