from django.db import models


# Create your models here.
class Section(models.Model):
    class Meta:
        verbose_name = "Rozdziały"
        verbose_name_plural = "Rozdział"

    section = models.CharField("Rozdział", max_length=5)
    name = models.CharField("Nazwa", max_length=20)

    def __str__(self):
        return f'{self.section} ({self.name})'


class Group(models.Model):
    class Meta:
        verbose_name = "Grupy"
        verbose_name_plural = "Grupa"

    group = models.CharField("Grupa", max_length=2)
    name = models.CharField("Nazwa", max_length=50)

    def __str__(self):
        return f'gr.{self.group}'


class Paragraph(models.Model):
    class Meta:
        verbose_name = "Paragrafy"
        verbose_name_plural = "Paragraf"

    paragraph = models.CharField("Paragraf", max_length=6)
    name = models.CharField("Nazwa", max_length=50, null=True)

    def __str__(self):
        return f'§{self.paragraph}'


class Source(models.Model):
    class Meta:
        verbose_name = "Źródła"
        verbose_name_plural = "Źródło"

    source = models.CharField("Źródło", max_length=80, null=True)

    def __str__(self):
        return f'{self.source}'


class Financesource(models.Model):
    class Meta:
        verbose_name = "Źródła finansowania"
        verbose_name_plural = "Źródła finansowania"

    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Rozdział")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupa")
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Paragraf")
    source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name="Źródło finansowania")

    def __str__(self):
        return f'{self.section} {self.paragraph} - {self.source}'
