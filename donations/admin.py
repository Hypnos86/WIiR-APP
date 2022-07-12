from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
from donations.models import TypeDonation, TypeFinancialResources, Application

# Register your models here.
admin.site.register(TypeDonation)
admin.site.register(TypeFinancialResources)


class ApplicationResource(resources.ModelResource):
    character = Field(attribute='character', column_name='Sprawa')
    date_receipt = Field(attribute='date_receipt', column_name='Data wpływu')
    date_return = Field(attribute='date_return', column_name='Data zwrotu')
    no_application = Field(attribute='no_application', column_name='Nr. wniosku')
    no_agreement = Field(attribute='no_agreement', column_name='Nr. porozumienia')
    date_agreement = Field(attribute='date_agreement', column_name='Data porozumienia')
    donation_type = Field(attribute='donation_type', column_name='Rodzaj daroziwny')
    financial_type = Field(attribute='financial_type', column_name='Rodzaj środków')
    presenter = Field(attribute='presenter', column_name='Darczyńca')
    sum = Field(attribute='sum', column_name='Kwota')
    settlement_date = Field(attribute='settlement_date', column_name='Data rozliczenia')
    unit = Field(attribute='unit', column_name='Jednostka')
    subject = Field(attribute='subject', column_name='Przedmiot porozumienia')

    class Meta:
        model = Application
        fields = ('character', 'date_receipt', 'date_return', 'no_application', 'no_agreement', 'date_agreement',
                  'donation_type', 'financial_type', 'presenter', 'sum', 'settlement_date', 'unit', 'subject')
        export_order = (
            'character', 'date_receipt', 'date_return', 'no_application', 'no_agreement', 'date_agreement',
            'donation_type', 'financial_type', 'presenter', 'sum', 'settlement_date', 'unit', 'subject')


@admin.register(Application)
class ContractorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'character', 'no_application', 'date_agreement', 'donation_type',
                    'financial_type', 'presenter', 'sum', 'unit', 'creation_date', 'change', 'author']
    search_fields = ['character', 'no_application', 'donation_type__type_name', 'presenter__name']
    list_display_links = ('character',)
    list_filter = ['donation_type', 'financial_type', 'unit__county__name']
    resource_class = ApplicationResource
