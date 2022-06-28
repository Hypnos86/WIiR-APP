from django.contrib import admin
from donations.models import TypeDonation, TypeFinancialResources, Application
# Register your models here.
admin.site.register(TypeDonation)
admin.site.register(TypeFinancialResources)
admin.site.register(Application)