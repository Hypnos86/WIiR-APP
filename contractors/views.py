from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Contractor
from .forms import ContractorsForm


class MakeContractorsListView(LoginRequiredMixin, View):
    template_name = 'contractors/contractor_list.html'
    paginate_by = 30

    def get(self, request, *args, **kwargs):
        contractors = Contractor.objects.all().order_by('name')
        contractor_len = len(contractors)

        paginator = Paginator(contractors, self.paginate_by)
        page_number = request.GET.get('page')
        contractors_list = paginator.get_page(page_number)

        try:
            last_date = Contractor.objects.values('change').latest('change')
        except Contractor.DoesNotExist:
            last_date = None

        query = "Wyczyść"
        search = "Szukaj"
        q = request.GET.get("q")

        if q:
            contractor = contractors.filter(name__icontains=q) \
                         | contractors.filter(city__icontains=q) \
                         | contractors.filter(no_contractor__startswith=q) \
                         | contractors.filter(nip__startswith=q)

            contractor_len = len(contractor)
            context = {'contractors': contractor, "consellsum": contractor_len, "query": query,
                       'last_date': last_date,
                       'q': q}
            return render(request, self.template_name, context)
        else:
            context = {'contractors': contractors_list, "consellsum": contractor_len, "search": search,
                       'last_date': last_date}
        return render(request, self.template_name, context)


class ShowInformationView(LoginRequiredMixin, View):
    template_name = 'contractors/information_popup.html'

    def get(self, request, id, *args, **kwargs):
        contractor = get_object_or_404(Contractor, pk=id)
        context = {'contractor': contractor, 'id': id}
        return render(request, self.template_name, context)


class AddNewContractorView(LoginRequiredMixin, View):
    template_name = 'contractors/contractor_form.html'
    form_class = ContractorsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'contractor_form': form, "new": True}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            return redirect('contractors:contractor_list')
        context = {'contractor_form': form, "new": True}
        return render(request, self.template_name, context)


class EditContractorView(LoginRequiredMixin, View):
    template_name = 'contractors/contractor_form.html'
    form_class = ContractorsForm

    def get(self, request, slug, *args, **kwargs):
        contractor = get_object_or_404(Contractor, slug=slug)
        form = self.form_class(instance=contractor)
        context = {'contractor_form': form, 'new': False}
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        contractor = get_object_or_404(Contractor, slug=slug)
        form = self.form_class(request.POST or None, instance=contractor)
        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.author = request.user
            form.save()
            return redirect('contractors:contractor_list')
        context = {'contractor_form': form, 'new': False}
        return render(request, self.template_name, context)
