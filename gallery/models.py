from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from investments.models import Project
import os


def upload_gallery(instance, filename):
    # return f'investments/{instance.gallery.project.project_title}/gallery/{instance.gallery.name}/{filename}'
    new_filename = create_name_photo(instance, filename)
    return f'investments/{instance.gallery.project.project_title}/gallery/{instance.gallery.name}/{new_filename}'


# Create your models here.
class Gallery(models.Model):
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerie'
        ordering = ['-name']

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery', verbose_name='Projekt INW')
    name = models.DateField('Nazwa galerii')
    add_date = models.DateField('Data dodania', auto_now_add=True)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='gallery', verbose_name='Autor')

    def __str__(self):
        return f'{self.project} ({self.name})'


class Photo(models.Model):
    class Meta:
        verbose_name = 'Zdjęcie'
        verbose_name_plural = 'Zdjęcia'
        ordering = ['add_date']

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='photo', verbose_name='Galeria')
    src = models.ImageField('Zdjęcie', upload_to=upload_gallery, max_length=300)
    add_date = models.DateField('Data dodania', auto_now_add=True)

    def __str__(self):
        return f'Zdjecie dodane {self.add_date}'


# @receiver(pre_save, sender=Photo)
def create_name_photo(instance, filename):
    extension = os.path.splitext(filename)
    new_filename = f'{instance.gallery.project.unit.city}_{instance.id}{extension}'
    return new_filename
