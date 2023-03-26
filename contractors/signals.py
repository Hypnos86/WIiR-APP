from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from contractors.models import Contractor


@receiver(pre_save, sender=Contractor)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        text = f'{instance.name} {instance.city}'
        instance.slug = slugify(text, )
