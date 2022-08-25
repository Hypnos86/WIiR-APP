from django.shortcuts import render


# Create your views here.
def contraction_inspection_menu(request):
    return render(request, "constructioninspections/navigation.html")
