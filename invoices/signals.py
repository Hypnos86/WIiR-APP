from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from invoices.models import InvoiceBuy, InvoiceItems
from decimal import Decimal


@receiver(post_save, sender=InvoiceItems)
def calculate_invoice_items_sum(sender, instance, **kwargs):
    cost = []
    items = InvoiceItems.objects.all()

    for item in items:
        if instance.invoice_id == item.invoice_id:
            cost.append(item.sum)
            print(instance)

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
            print(instance)

    invoice = InvoiceBuy.objects.get(pk=instance.invoice_id.id)
    invoice.sum = sum(cost)
    invoice.save()