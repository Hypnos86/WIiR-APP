from django.urls import path
from constructioninspections.views import create_buildings_one_year_inspections_list, buildings_inspections_choice, \
    create_buildings_five_year_inspections_list, create_chimney_inspection_list, \
    create_electrical_inspection_one_year_list, create_heating_boilers_inspection_list, \
    create_air_conditioners_inspection_list, create_fire_inspection_list, important_inspections, \
    create_electrical_inspection_five_year_list, electrical_inspections_choice, add_protocol_buildings_inspections_one_year

app_name = "constructioninspections"
urlpatterns = [
    # Menu
    path("", important_inspections, name="important_inspections"),
    # Popapy do wybierania rocznych lub pięcioletnich protokołów
    path("buildings_inspections_choice_popup/", buildings_inspections_choice,
         name="buildings_inspections_choice"),
    path("electrical_inspections_choice_popup/", electrical_inspections_choice,
         name="electrical_inspections_choice"),
    # Przeglądy budynków - roczne
    path("buildings_inspections_one_year/", create_buildings_one_year_inspections_list,
         name="create_buildings_one_year_inspections_list"),
    path("add_protocol_buildings_one_year/", add_protocol_buildings_inspections_one_year,
         name="add_protocol_buildings_inspections_one_year"),
    # Przeglądy budynków - pięcioletnie
    path("buildings_inspections_five_year/", create_buildings_five_year_inspections_list,
         name="create_buildings_five_year_inspections_list"),
    # Przeglądy kominowe
    path("chimneys_inspections/", create_chimney_inspection_list, name="create_chimney_inspection_list"),
    # Przeglądy elektryczne - roczne
    path("electrical_inspections_one_year/", create_electrical_inspection_one_year_list,
         name="create_electrical_inspection_one_year_list"),
    # Przeglądy elektryczne - pięcioletnie
    path("electrical_inspections_five_year/", create_electrical_inspection_five_year_list,
         name="create_electrical_inspection_five_year_list"),
    # Przeglądy kotłów
    path("heating_boilers_inspections/", create_heating_boilers_inspection_list,
         name="create_heating_boilers_inspection_list"),
    # Przeglądy klimatyzacji
    path("air_conditioners_inspections/", create_air_conditioners_inspection_list,
         name="create_air_conditioners_inspection_list"),
    # Przeglądy p.poż
    path("create_fire_inspections/", create_fire_inspection_list, name="create_fire_inspection_list"),

]
