from django.urls import path
from constructioninspections.views import create_buildings_one_year_inspections_list, buildings_inspections_choice, \
    create_buildings_five_year_inspections_list, create_chimney_inspection_list, \
    create_electrical_inspection_one_year_list, create_heating_boilers_inspection_list, \
    create_air_conditioners_inspection_list, create_fire_inspection_list, important_inspections, \
    create_electrical_inspection_five_year_list, electrical_inspections_choice, add_protocol, show_information, edit_protocol, priority_inspections_list

app_name = "constructioninspections"
urlpatterns = [
    # Menu
    path("", important_inspections, name="important_inspections"),
    # Njapilniejsze przeglady
    path("upcomingReviews/<int:typeInspection>/", priority_inspections_list, name="priority_inspections_list"),
    # Popapy do wybierania rocznych lub pięcioletnich protokołów
    path("buildingsInspectionsChoicePopup/", buildings_inspections_choice,
         name="buildings_inspections_choice"),
    path("electricalInspectionsChoicePopup/", electrical_inspections_choice,
         name="electrical_inspections_choice"),
    # Dodanie nowego protokołu
    path("addProtocol/<int:typeInspection>", add_protocol,
         name="add_protocol"),
    # Edytowanie protokołu
    path("editProtocol/<int:typeInspection>/<int:id>/", edit_protocol, name="edit_protocol"),
    # Przeglądy budynków - roczne
    path("buildingsInspectionsOneYear/", create_buildings_one_year_inspections_list,
         name="create_buildings_one_year_inspections_list"),
    # Przeglądy budynków - pięcioletnie
    path("buildingsInspectionsFiveYear/", create_buildings_five_year_inspections_list,
         name="create_buildings_five_year_inspections_list"),
    # Przeglądy kominowe
    path("chimneysInspections/", create_chimney_inspection_list, name="create_chimney_inspection_list"),
    # Przeglądy elektryczne - roczne
    path("electricalInspectionsOneYear/", create_electrical_inspection_one_year_list,
         name="create_electrical_inspection_one_year_list"),
    # Przeglądy elektryczne - pięcioletnie
    path("electricalInspectionsFiveYear/", create_electrical_inspection_five_year_list,
         name="create_electrical_inspection_five_year_list"),
    # Przeglądy kotłów
    path("heatingBoilersInspections/", create_heating_boilers_inspection_list,
         name="create_heating_boilers_inspection_list"),
    # Przeglądy klimatyzacji
    path("airConditionersInspections/", create_air_conditioners_inspection_list,
         name="create_air_conditioners_inspection_list"),
    # Przeglądy p.poż
    path("createFireInspections/", create_fire_inspection_list, name="create_fire_inspection_list"),
    # Popup informacyjny
    path("info/<int:typeInspection>/<int:id>", show_information, name="show_information")

]
