import datetime

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from invoices.models import InvoiceBuy, InvoiceItems, InvoiceSell
from decimal import Decimal


@receiver(post_save, sender=InvoiceItems)
def calculate_invoice_items_sum(sender, instance, **kwargs):
    cost = []
    items = InvoiceItems.objects.all()

    for item in items:
        if instance.invoice_id == item.invoice_id:
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


# @receiver(pre_save, sender=InvoiceSell)
# def addDayToDateField(sender, instance, **kwargs):
#     print(instance.period_from[0:4])
#     print(instance.period_from[5:7])
#     # print(datetime.datetime(year=int(instance.period_from[0:4]), month=int(instance.period_from[5:7]), day=1))
#     x = datetime.date(year=int(instance.period_from[0:4]), month=int(instance.period_from[5:7]), day=1).__str__()
#
#     instance.period_from = x
#     # instance.period_from = datetime.date(year=int(instance.period_from[0:4]), month=int(instance.period_from[5:7]), day=1)
#     # print(instance.period_from)
#     instance.save()
