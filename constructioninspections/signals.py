from django.db.models.signals import pre_save
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta
from constructioninspections.models import BuildingInspectionOneYear, BuildingInspectionFiveYear, \
    ElectricalInspectionOneYear, ElectricalInspectionFiveYear, ChimneyInspection, FireInspection, \
    AirConditionerInspection, HeatingBoilerInspection


@receiver(pre_save, sender=BuildingInspectionOneYear)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=BuildingInspectionFiveYear)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=ElectricalInspectionOneYear)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=ElectricalInspectionFiveYear)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=ChimneyInspection)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=FireInspection)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=AirConditionerInspection)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)


@receiver(pre_save, sender=HeatingBoilerInspection)
def add_next_date_protocol(sender, instance, **kwargs):
    instance.date_next_inspection = instance.date_protocol + relativedelta(months=12)
