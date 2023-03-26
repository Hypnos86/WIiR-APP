from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from businessflats.models import OfficialFlat


@receiver(pre_save, sender=OfficialFlat)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        text = f'{instance.address} {instance.city}'
        instance.slug = slugify(text, )
