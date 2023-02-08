import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import NeedsLetter


@receiver(pre_save, sender=NeedsLetter)
def save_is_done(sender, instance, **kwargs):
    if instance.execution_date:
        instance.isDone = True

    if instance.cost == None:
        instance.cost = 0
