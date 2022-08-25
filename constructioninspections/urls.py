from django.urls import path
from constructioninspections.views import contraction_inspection_menu

app_name = "constructioninspections"
urlpatterns = [
    path("inspections_menu/", contraction_inspection_menu, name="contraction_inspection_menu")

]
