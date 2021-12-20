from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Team, Telephone


# Create your views here.
@login_required
def telephone_list(request):
    teams = Team.objects.all()
    tel = Telephone.objects.all()

    context = {'tel': tel,
               'teams': teams}
    return render(request, 'main/telephones.html', context)


@login_required
def welcome(request):
    return render(request, 'main/welcome.html', {})
