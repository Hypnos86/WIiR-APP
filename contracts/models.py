from django.db import models


class Stan(models.Model):
    class Meta:
        verbose_name = "Stan umowy"
        verbose_name_plural = "Stany umów"

    stan = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.stan}'


class Rodzaj(models.Model):
    class Meta:
        verbose_name = "Rodzaj umowy"
        verbose_name_plural = "Rodzaje umów"

    rodzaj = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rodzaj}'


class Podstawa(models.Model):
    class Meta:
        verbose_name = "Podstawa prawna"
        verbose_name_plural = "Podstawy prawne"

    podstawa = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.podstawa}'


class Contractimmovables(models.Model):
    class Meta:
        verbose_name = "Umowa nieruchomosci"
        verbose_name_plural = "Umowy nieruchomosci"

    data_umowy = models.DateField("Data umowy")
    nrumowy = models.CharField(max_length=20, blank=True, default="BRAK")
    kontrahent = models.ForeignKey("contractors.Contractorsell", on_delete=models.CASCADE)
    podstawa = models.ForeignKey("contracts.Podstawa", on_delete=models.CASCADE, blank=True)
    okres_obowiazywania = models.DateField("Okres obowiązywania", null=True, blank=True)
    rodzaj = models.ForeignKey("contracts.Rodzaj", on_delete=models.CASCADE)
    pow_uzyczona = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    koszt_prad = models.BooleanField()
    inf_prad = models.TextField(blank=True, default="")
    koszt_gaz = models.BooleanField()
    inf_gaz = models.TextField(blank=True, default="")
    koszt_woda = models.BooleanField()
    inf_woda = models.TextField(blank=True, default="")
    koszt_co = models.BooleanField()
    inf_co = models.TextField(blank=True, default="")
    unit = models.ForeignKey("units.Unit", on_delete=models.CASCADE, null=False)
    skan = models.FileField(upload_to='umowy_pdf', null=True, blank=True)
    stan = models.ForeignKey("contracts.Stan", on_delete=models.CASCADE, blank=False, default=1)
    comments = models.TextField("Uwagi", blank=True, default="")
    archives = models.BooleanField(null=False, default=0)
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    autor = models.ForeignKey("auth.User", editable=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'Umowa z dnia {self.data_umowy} zawarta z {self.kontrahent}'
