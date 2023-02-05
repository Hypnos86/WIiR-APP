from django.db.models.signals import pre_save
from django.dispatch import receiver
from contracts.models import ContractAuction, FinancialDocument
from decimal import Decimal


@receiver(pre_save, sender=ContractAuction)
def calculate_security_sum(sender, instance, **kwargs):
    try:
        instance.security_sum = instance.price * instance.security_percent * Decimal(0.01)
    except TypeError:
        instance.security_sum = None

@receiver(pre_save, sender=FinancialDocument)
def calculate_tax(sender,instance, **kwargs):
    try:
        instance.cost_brutto = instance.cost_netto * (instance.vat.vat * Decimal(0.01)) + instance.cost_netto
    except TypeError:
        instance.cost_brutto = None

