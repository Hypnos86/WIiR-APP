from django.db.models.signals import pre_save
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta
from constructioninspections.models import BuildingInspectionOneYear


@receiver(pre_save, sender=BuildingInspectionOneYear)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)
