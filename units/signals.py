from django.db.models.signals import pre_save
from django.dispatch import receiver
from units.models import Unit


@receiver(pre_save, sender=Unit)
def create_full_name_unit(sender, instance, **kwargs):
    instance.full_name = f'{instance.type}  {instance.city} - {instance.address}'
