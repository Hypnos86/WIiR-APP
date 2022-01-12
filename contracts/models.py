from django.db import models
from units.models import Unit


# my models
class Stan(models.Model):
    class Meta:
        verbose_name = "Stan umowy"
        verbose_name_plural = "Nieruchomości - Stany umów"

    stan = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.stan}'


class Rodzaj(models.Model):
    class Meta:
        verbose_name = "Rodzaj umowy"
        verbose_name_plural = "Nieruchomości - Rodzaje umów"

    rodzaj = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rodzaj}'


class Podstawa(models.Model):
    class Meta:
        verbose_name = "Podstawa prawna"
        verbose_name_plural = "Nieruchomosci - Podstawy prawne"

    podstawa = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.podstawa}'


class LegalBasicZzp(models.Model):
    class Meta:
        verbose_name = "Podstawa prawna ZZP"
        verbose_name_plural = "Umowy ZZP - Tryb zamówień"

    legal_basic_zzp = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.legal_basic_zzp}'


class Guarantee(models.Model):
    class Meta:
        verbose_name = 'Gwarancja'
        verbose_name_plural = 'Umowy ZZP - Gwarancje'

    guarantee = models.CharField('Gwarancja', max_length=50)

    def __str__(self):
        return f'{self.guarantee}'


class Period(models.Model):
    class Meta:
        verbose_name = 'Okres'
        verbose_name_plural = 'Umowy ZZP - Okresy'

    period = models.SmallIntegerField('Okres (mc)', null=True)

    def __str__(self):
        return f'{self.period}'


class GuaranteePeriod(models.Model):
    guarantee_period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='GuaranteePeriod', verbose_name='Okres gwarancji')

    def __str__(self):
        return f'{self.guarantee_period}'


class WarrantyPeriod(models.Model):
    pass


class ContractImmovables(models.Model):
    class Meta:
        verbose_name = "Umowa nieruchomosci"
        verbose_name_plural = "Nieruchomości - Umowy"
        ordering = ['data_umowy']

    data_umowy = models.DateField("Data")
    nrumowy = models.CharField("Nr umowy", max_length=20, null=True, blank=True, default="")
    kontrahent = models.ForeignKey("contractors.Contractor", on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name="contractimmovables")
    podstawa = models.ForeignKey("contracts.Podstawa", on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Podstawa prawna", related_name="contractimmovables")
    okres_obowiazywania = models.DateField("Okres obowiązywania", null=True, blank=True)
    rodzaj = models.ForeignKey("contracts.Rodzaj", on_delete=models.CASCADE, verbose_name="Rodzaj umowy",
                               related_name="contractimmovables")
    pow_uzyczona = models.DecimalField("Powierzchnia użytkowa", max_digits=8, decimal_places=2, null=True, blank=True)
    koszt_czynsz = models.BooleanField("Czynsz")
    koszt_prad = models.BooleanField("Prąd")
    koszt_gaz = models.BooleanField("Gaz")
    koszt_woda = models.BooleanField("Woda")
    koszt_co = models.BooleanField("C.O.")
    koszt_smieci = models.BooleanField("Śmieci")
    koszt_podsmiec = models.BooleanField("Zagospodarowanie odpadami komunalnymi")
    koszt_podnier = models.BooleanField("Podatek od nieruchomości")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False, verbose_name="Jednostka",
                             related_name="contractimmovables")
    skan = models.FileField(upload_to='contracts_immovables/%Y/', null=True, blank=True, verbose_name="Skan umowy")
    stan = models.ForeignKey(Stan, on_delete=models.CASCADE, blank=False, default=1, related_name="contractimmovables")
    comments = models.TextField("Informacje", blank=True, default="")
    archives = models.BooleanField("Aktywna", null=False, default=1)
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="contractimmovables",
                               verbose_name="author")

    def __str__(self):
        return f'Umowa z dnia {self.data_umowy} ({self.kontrahent})'


class AneksImmovables(models.Model):
    class Meta:
        verbose_name = 'Aneks'
        verbose_name_plural = 'Nieruchomosci - Aneksy'
        ordering = ['contractimmovables', 'data_aneksu']

    contractimmovables = models.ForeignKey('contracts.ContractImmovables', on_delete=models.CASCADE,
                                           verbose_name='Umowa',
                                           related_name='aneks')
    skan_aneksu = models.FileField(upload_to='contracts_immovables/annexes/%Y/', null=True, blank=True,
                                   verbose_name='Skan aneks')
    data_aneksu = models.DateField('Data aneksu', null=True)
    create = models.DateTimeField('Data utworzenia', auto_now_add=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data_aneksu} {self.skan_aneksu}'


class ContractAuction(models.Model):
    class Meta:
        verbose_name = 'Umowa ZZP'
        verbose_name_plural = 'Umowy ZZP'
        ordering = ['date']

    date = models.DateField('Data')
    no_contract = models.CharField('Nr. umowy', max_length=20)
    contractor = models.ForeignKey('contractors.Contractor', on_delete=models.CASCADE,
                                   verbose_name='Kontrahent',
                                   related_name='contract_auction')
    price = models.DecimalField('Wartość umowy', max_digits=12, decimal_places=2)
    work_scope = models.CharField('Zakres', max_length=120)
    legal_basic_zzp = models.ForeignKey(LegalBasicZzp, on_delete=models.CASCADE, related_name='contract_auction',
                                        verbose_name='Tryb UPZP')
    end_date = models.DateField('Data zakończenia')

    unit = models.ForeignKey('units.Unit', on_delete=models.CASCADE, verbose_name='Jednostka',
                             related_name='contract_auction')
    last_report_date = models.DateField('Data ostatniego protokołu')
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, verbose_name='Gwarancja',
                                  related_name='contract_auction')
    guarantee_period = models.ForeignKey(GuaranteePeriod, on_delete=models.CASCADE, verbose_name='Okres gwarancji',
                                         related_name='contract_auction')
    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.CASCADE, verbose_name='Okres rękojmi',
                                        related_name='contract_auction')
    security_percent = models.SmallIntegerField('Procent zabezpiecznia')
    contract_security = models.DecimalField('Kwota zabezpiecznia', max_digits=10, decimal_places=2)
    inspector = models.ManyToManyField('main.Inspector', verbose_name='Inspektor', related_name='ContractAuction')
    raport = models.TextField('Raportowanie', blank=True, default='')
    information = models.TextField('Informacje', blank=True, default='')
    scan = models.FileField(upload_to='contracts_zzp/%Y/', null=True, blank=True, verbose_name='Skan umowy')
    create = models.DateTimeField('Data utworzenia', auto_now_add=True)
    change = models.DateTimeField('Zmiana', auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='contract_auction',
                               verbose_name="author")

    def __str__(self):
        return f'{self.no_contract} z dnia {self.date}'


class AneksContractAuction(models.Model):
    class Meta:
        verbose_name = 'Aneks ZZP'
        verbose_name_plural = 'Umowy ZZP (Aneksy)'
        ordering = ['contract_auction', 'date']

    contract_auction = models.ForeignKey(ContractAuction, on_delete=models.CASCADE,
                                         verbose_name='Umowa ZZP',
                                         related_name='aneks_contract_auction')
    date = models.DateField('Data aneksu', null=True)
    price_change = models.BooleanField('Zmiana wartości umowy', default=False)
    price_after_change = models.DecimalField('Kwota aneksu', max_digits=10, decimal_places=2)
    scope_changes = models.TextField('Zakres zmian', blank=True, default='')
    scan = models.FileField(upload_to='contracts_zzp/annexes/%Y/', null=True, blank=True,
                            verbose_name='Skan aneksu')
    create = models.DateTimeField('Data utworzenia', auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'Aneks z dnia {self.date} {self.scan}'
