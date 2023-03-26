from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from donations.models import Application


@receiver(pre_save, sender=Application)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        text = f'{instance.character} {instance.financial_type}'
        instance.slug = slugify(text, )
