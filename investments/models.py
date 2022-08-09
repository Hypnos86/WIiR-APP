from django.db import models
from tinymce import models as tinymce_models
from units.models import Unit
from sourcefinancing.models import Section, Group, Paragraph
from main.models import Employer


def upload_scan(instance, filename):
    return f"investments/{instance.project_title}/{filename}"


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = "Zadanie inwestycyjne"
        verbose_name_plural = "Zadania inwestycyjne"
        ordering = ["date_of_acceptance"]

    date_of_acceptance = models.DateField("Data programu", null=True, blank=True)
    no_acceptance_document = models.CharField("L.dz. programu", max_length=15, null=True, blank=True)
    investment_program = models.FileField(upload_to=upload_scan, null=True, blank=True,
                                          verbose_name="Program inwestycji")
    project_title = models.CharField("Pełna nazwa zadania", max_length=300, null=True, blank=True)
    investment_cost_estimate_value = models.DecimalField("WKI", max_digits=12, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="project", verbose_name="Jednostka")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="project", verbose_name="Rozdział")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="project", verbose_name="Grupa")
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name="project",
                                  verbose_name="Paragraf")
    source_financing = tinymce_models.HTMLField("Źródło finansowania", null=True, blank=True)
    information = tinymce_models.HTMLField("Informacje", null=True, blank=True)
    date_of_settlement = models.DateField("Data rozliczenia", null=True, blank=True)
    settlement_scan = models.FileField(upload_to=upload_scan, null=True, blank=True,
                                       verbose_name="Rozliczenie inwestycyjne")
    realized = models.BooleanField("Zrealizowane", default=False)
    worker = models.ManyToManyField(Employer, verbose_name="Inspektor", related_name="project")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="project", verbose_name="Autor")

    def __str__(self):
        return f"{self.project_title}"

