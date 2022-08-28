from django.contrib import admin
from constructioninspections.models import TechnicalCondition, TypeInspection,BuildingInspection

# Register your models here.
admin.site.register(TechnicalCondition)
admin.site.register(TypeInspection)
admin.site.register(BuildingInspection)