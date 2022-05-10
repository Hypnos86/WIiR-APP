from django.db import models


# Create your models here.
class County(models.Model):
    class Meta:
        verbose_name = 'Powiat'
        verbose_name_plural = 'Powiaty'
        ordering = ['swop_id']

    swop_id = models.CharField(max_length=4, unique=True, verbose_name='ID SWOP')
    name = models.CharField(max_length=15, null=False, verbose_name='Powiat')

    def __str__(self):
        return f'{self.name}'


class TypeUnit(models.Model):
    class Meta:
        verbose_name = "Rodzaj jednostki"
        verbose_name_plural = "Rodzaje jednostek"
        ordering = ['id']

    type_short = models.CharField(max_length=10, null=False, verbose_name='Skrócona nazwa')
    type_full = models.CharField(max_length=30, null=False, verbose_name='Pełna nazwa')

    def __str__(self):
        return f'{self.type_short}'


class Unit(models.Model):
    class Meta:
        verbose_name = 'Jednostka'
        verbose_name_plural = 'Jednostki'
        ordering = ['county']

    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='unit')
    type = models.ForeignKey(TypeUnit, on_delete=models.CASCADE, related_name='unit')
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    information = models.TextField(blank=True)
    manager = models.CharField(max_length=50)
    status = models.BooleanField('Status', null=False, default=0)
    change = models.DateTimeField('Zmiany', auto_now=True)

    def __str__(self):
        return f'{self.information} - {self.city}, {self.address}'
