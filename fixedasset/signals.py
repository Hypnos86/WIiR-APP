from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from fixedasset.models import Building


@receiver(pre_save, sender=Building)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        text = f'{instance.no_inventory} {instance.building_name}'
        instance.slug = slugify(text, )
