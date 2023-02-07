from django.db import models


# Create your models here.
class Section(models.Model):
    class Meta:
        verbose_name = "Rozdział"
        verbose_name_plural = "K.02 - Rozdziały"
        ordering = ["section"]

    section = models.CharField("Rozdział", max_length=5, unique=True)
    name = models.CharField("Nazwa", max_length=20)

    def __str__(self):
        return f"{self.section} ({self.name})"


class Group(models.Model):
    class Meta:
        verbose_name = "Grupa"
        verbose_name_plural = "K.01 - Grupy"

    group = models.CharField("Grupa", max_length=2, unique=True)
    name = models.CharField("Nazwa", max_length=50)

    def __str__(self):
        return f"gr.{self.group}"


class Paragraph(models.Model):
    class Meta:
        verbose_name = "Paragraf i pozycja"
        verbose_name_plural = "K.03 - Paragrafy i pozycje"

    paragraph = models.CharField("Paragraf", max_length=7, unique=True)
    name = models.CharField("Nazwa", max_length=50)

    def __str__(self):
        return f"{self.paragraph}"


class Source(models.Model):
    class Meta:
        verbose_name = "Źródło finansowania"
        verbose_name_plural = "K.04 - Źródła finansowania"

    source = models.CharField("Źródło", max_length=80, null=True, unique=True)

    def __str__(self):
        return f"{self.source}"


class FinanceSource(models.Model):
    class Meta:
        verbose_name = "Konto"
        verbose_name_plural = "K.05 - Konta"

    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Rozdział")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupa")
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Paragraf")
    source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name="Źródło finansowania")

    def __str__(self):
        return f"{self.section.section}-{self.group.group}-{self.paragraph}-{self.source}"
