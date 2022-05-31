from django.db import models
from units.models import Unit
from sourcefinancing.models import Section, Group, Paragraph
from main.models import Employer


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = 'Zadanie inwestycyjne'
        verbose_name_plural = 'Zadania inwestycyjne'
        ordering = ['date_of_acceptance']

    date_of_acceptance = models.DateField('Data programu', null=True, blank=True)
    no_acceptance_document = models.CharField('L.dz. programu', max_length=15, null=True, blank=True)
    investment_program = models.FileField(upload_to='investments/investment_program/%Y/', null=True, blank=True,
                                          verbose_name='Program inwestycji')
    project_title = models.CharField('Pełna nazwa zadania', max_length=200, null=True, blank=True)
    investment_cost_estimate_value = models.DecimalField('WKI', max_digits=12, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='project', verbose_name='Jednostka')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='project', verbose_name='Rozdział')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='project', verbose_name='Grupa')
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='project',
                                  verbose_name='Paragraf')
    source_financing = models.TextField('Opis źródła finansowania', null=True, blank=True)
    information = models.TextField('Informacje', null=True, blank=True)
    worker = models.ManyToManyField(Employer, related_name='project', verbose_name='Branżysta')
    date_of_settlement = models.DateField('Data rozliczenia', null=True, blank=True)
    settlement_scan = models.FileField(upload_to='investments/settlements/%Y/', null=True, blank=True,
                                       verbose_name='Rozliczenie inwestycyjne')
    realized = models.BooleanField('Zrealizowane', default=False)
    creation_date = models.DateTimeField('Data utworzenia', auto_now_add=True)
    change = models.DateField('Zmiana', auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='project', verbose_name='Autor')

    def __str__(self):
        return f'{self.unit} - {self.project_title}'


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery', verbose_name='Id inwestycji')
    add_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to=f'Gallery/{{Project}}/%Y/%m')
    pass
