from django.urls import path
from constructioninspections.views import BuildingsOneYearInspectionsList, BuildingsInspectionsChoice, \
    BuildingsFiveYearInspectionsList, ChimneyInspectionList, \
    ElectricalInspectionOneYearList, HeatingBoilersInspectionList, \
    AirConditionersInspectionList, FireInspectionList, ImportantInspections, \
    ElectricalInspectionFiveYearList, ElectricalInspectionsChoice, add_protocol, ShowInformationProtocolView, \
    edit_protocol, PriorityInspectionsList

app_name = "constructioninspections"
urlpatterns = [
    # Menu
    path("", ImportantInspections.as_view(), name="important_inspections"),
    # Njapilniejsze przeglady
    path("upcoming/<int:typeInspection>/", PriorityInspectionsList.as_view(), name="priority_inspections_list"),
    # Popapy do wybierania rocznych lub pięcioletnich protokołów
    path("buildingsInspectionsChoicePopup/", BuildingsInspectionsChoice.as_view(),
         name="buildings_inspections_choice"),
    path("electricalInspectionsChoicePopup/", ElectricalInspectionsChoice.as_view(),
         name="electrical_inspections_choice"),
    # Dodanie nowego protokołu
    path("add/<int:typeInspection>", add_protocol,
         name="add_protocol"),
    # Edytowanie protokołu
    path("edit/<int:typeInspection>/<int:id>/", edit_protocol, name="edit_protocol"),
    # Przeglądy budynków - roczne
    path("buildingsOneYear/", BuildingsOneYearInspectionsList.as_view(),
         name="create_buildings_one_year_inspections_list"),
    # Przeglądy budynków - pięcioletnie
    path("buildingsFiveYear/", BuildingsFiveYearInspectionsList.as_view(),
         name="create_buildings_five_year_inspections_list"),
    # Przeglądy kominowe
    path("chimneys/", ChimneyInspectionList.as_view(), name="create_chimney_inspection_list"),
    # Przeglądy elektryczne - roczne
    path("electricalOneYear/", ElectricalInspectionOneYearList.as_view(),
         name="create_electrical_inspection_one_year_list"),
    # Przeglądy elektryczne - pięcioletnie
    path("electricalFiveYear/", ElectricalInspectionFiveYearList.as_view(),
         name="create_electrical_inspection_five_year_list"),
    # Przeglądy kotłów
    path("heatingBoilers/", HeatingBoilersInspectionList.as_view(),
         name="create_heating_boilers_inspection_list"),
    # Przeglądy klimatyzacji
    path("airConditioners/", AirConditionersInspectionList.as_view(),
         name="create_air_conditioners_inspection_list"),
    # Przeglądy p.poż
    path("FireInspections/", FireInspectionList.as_view(), name="create_fire_inspection_list"),
    # Popup informacyjny
    path("info/<int:typeInspection>/<int:id>", ShowInformationProtocolView.as_view(), name="show_information")

]
