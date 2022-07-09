from django.db.models.signals import pre_save
from django.dispatch import receiver
from cpvdict.models import Order
from decimal import Decimal


@receiver(pre_save, sender=Order)
def calculate_order(sender, instance, **kwargs):
    instance.sum_brutto = instance.sum_netto * instance.vat.vat * Decimal(0.01) + instance.sum_netto
