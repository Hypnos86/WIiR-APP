from django.shortcuts import render
from main.models import Team, Telephone


# Create your views here.
def telephone_list(request):
    teams = Team.objects.all()
    tel = Telephone.objects.all()

    context = {'tel': tel,
               'teams': teams}
    return render(request, 'main/telephones.html', context)
