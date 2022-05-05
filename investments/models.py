from django.db import models
from units.models import Unit
from sourcefinancing.models import Section, Group, Paragraph


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = 'Zadanie inwestycyjne'
        verbose_name_plural = 'Zadania inwestycyjne'
        ordering = ['date_of_acceptance']

    date_of_acceptance = models.DateField('Data pisma', null=True, blank=True)
    no_acceptance_document = models.CharField('Liczba pisma', max_length=15, null=True, blank=True)
    investment_program = models.FileField(upload_to='investment_program/%Y/', null=True, blank=True,
                                          verbose_name='Program inwestycji')
    project_title = models.CharField('Nazwa zadania', max_length=200, null=True, blank=True)
    investment_cost_estimate_value = models.DecimalField('WKI', max_digits=12, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='project', verbose_name='Jednostka')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='project', verbose_name='Rozdział')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='project', verbose_name='Grupa')
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='project',
                                  verbose_name='Paragraf')
    source_financing = models.TextField('Opis źródła finansowania', null=True, blank=True)
    information = models.TextField('Informacje', null=True, blank=True)
    creation_date = models.DateTimeField('Data utworzenia', auto_now_add=True)

    def __str__(self):
        return f'{self.unit} - {self.project_title}'
