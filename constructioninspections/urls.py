from django.urls import path
from constructioninspections.views import contraction_inspection_menu, create_buildings_inspections_choise, \
    create_buildings_one_year_inspections, create_buildings_five_year_inspections, create_chimney_inspection_list, \
    create_electrical_inspection_list, create_heating_boilers_inspection_list, create_air_conditioners_inspection_list, \
    create_fire_inspection_list

app_name = "constructioninspections"
urlpatterns = [
    path("inspections_menu/", contraction_inspection_menu, name="contraction_inspection_menu"),
    path("buildings_inspections_choise/", create_buildings_inspections_choise, name="create_buildings_inspections_choise"),
    path("buildings_inspections_one_year/", create_buildings_one_year_inspections, name="create_buildings_one_year_inspections"),
    path("buildings_inspections_five_year/", create_buildings_five_year_inspections, name="create_buildings_five_year_inspections"),
    path("chimneys_inspections/", create_chimney_inspection_list, name="create_chimney_inspection_list"),
    path("electrical_inspections/", create_electrical_inspection_list, name="create_electrical_inspection_list"),
    path("heating_boilers_inspections/", create_heating_boilers_inspection_list, name="create_heating_boilers_inspection_list"),
    path("air_conditioners_inspections/", create_air_conditioners_inspection_list, name="create_air_conditioners_inspection_list"),
    path("create_fire_inspections/", create_fire_inspection_list, name="create_fire_inspection_list"),
]
