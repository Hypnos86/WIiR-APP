import datetime

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from invoices.models import InvoiceBuy, InvoiceItems, InvoiceSell
from decimal import Decimal


@receiver(post_save, sender=InvoiceItems)
def sumInvoiceItems(sender, instance, **kwargs):
    cost = []
    items = InvoiceItems.objects.filter(invoice_id=instance.invoice_id)

    for item in items:
        cost.append(item.sum)

    invoice = InvoiceBuy.objects.get(pk=instance.invoice_id.id)
    invoice.sum = sum(cost)
    invoice.save()


@receiver(post_delete, sender=InvoiceItems)
def delete_invoice_item(sender, instance, **kwargs):
    cost = []
    items = InvoiceItems.objects.all()

    for item in items:
        if instance.invoice_id == item.invoice_id:
            cost.append(item.sum)

    invoice = InvoiceBuy.objects.get(pk=instance.invoice_id.id)
    invoice.sum = sum(cost)
    invoice.save()
