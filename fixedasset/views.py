from django.shortcuts import render


# Create your views here.
def fixed_asset_list(request):
    return render(request, "fixedasset/fixed_asset_list.html")
