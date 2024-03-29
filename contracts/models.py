from django.db import models
from units.models import Unit
from main.models import Employer
from contractors.models import Contractor
from investments.models import Project
from cpvdict.models import Tax


class TypeOfContract(models.Model):
    class Meta:
        verbose_name = "Rodzaj umowy"
        verbose_name_plural = "U.03 - Umowy Nieruchomości - Rodzaje umów"

    type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.type}"


class LegalBasic(models.Model):
    class Meta:
        verbose_name = "Podstawa prawna"
        verbose_name_plural = "U.13 - Podstawy prawne"

    act = models.CharField(max_length=100, null=False, verbose_name="Ustawa")
    legal_basic = models.CharField(max_length=30, null=False, verbose_name="Paragraf w ustawie")
    legal_basic_text = models.TextField(null=False, verbose_name="Tekst paragrafu")

    def __str__(self):
        return f"{self.act} - {self.legal_basic}"


class Guarantee(models.Model):
    class Meta:
        verbose_name = "Gwarancja"
        verbose_name_plural = "U.12 - Umowy ZZP - Rodzaje Gwarancji"
        ordering = ["guarantee"]

    guarantee = models.CharField("Gwarancja", max_length=50)

    def __str__(self):
        return f"{self.guarantee}"


def upload_scan_contract_immovables(instance, filename):
    extension = filename.split(".")[-1]
    return f"contracts_immovables/{instance.unit.city}/{instance.id}.Umowa_z_dnia_{instance.date.strftime('%d.%m.%Y')}.{extension}"


class ContractImmovables(models.Model):
    class Meta:
        verbose_name = "Umowa nieruchomosci"
        verbose_name_plural = "U.01 - Umowy Nieruchomości"
        ordering = ["date"]

    date = models.DateField("Data")
    no_contract = models.CharField("Nr umowy", max_length=20, null=True, blank=True, default="")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Kontrahent",
                                   related_name="contractimmovables")
    legal_basic = models.ForeignKey(LegalBasic, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="Podstawa prawna", related_name="contractimmovables")
    period_of_validity = models.DateField("Okres obowiązywania", null=True, blank=True)
    type_of_contract = models.ForeignKey(TypeOfContract, on_delete=models.CASCADE, verbose_name="Rodzaj umowy",
                                         related_name="contractimmovables")
    usable_area = models.DecimalField("Powierzchnia użytkowa", max_digits=8, decimal_places=2, null=True, blank=True)
    rent_cost = models.BooleanField("Czynsz")
    electric_cost = models.BooleanField("Prąd")
    gas_cost = models.BooleanField("Gaz")
    water_cost = models.BooleanField("Woda")
    central_heating_cost = models.BooleanField("C.O.")
    garbage_cost = models.BooleanField("Śmieci")
    garbage_tax_cost = models.BooleanField("Zagospodarowanie odpadami komunalnymi")
    property_cost = models.BooleanField("Podatek od nieruchomości")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False, verbose_name="Jednostka",
                             related_name="contractimmovables")
    scan = models.FileField(upload_to=upload_scan_contract_immovables, null=True, blank=True, verbose_name="Skan umowy")
    state = models.BooleanField(default=True, verbose_name="Aktualna")
    information = models.TextField("Informacje", blank=True, default="")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="contractimmovables",
                               verbose_name="Autor")

    def __str__(self):
        return f"Umowa z dnia {self.date.strftime('%d.%m.%Y')} ({self.contractor})"


def upload_scan_annex_contract_immovables(instance, filename):
    extension = filename.split(".")[-1]
    return f"contracts_immovables/{instance.contract_immovables.unit.city}/{instance.contract_immovables.id}.Aneks_z_dnia_{instance.date_annex.strftime('%d.%m.%Y')}.{extension}"


class AnnexImmovables(models.Model):
    class Meta:
        verbose_name = "Aneks na umowę nieruchomości"
        verbose_name_plural = "U.02 - Umowy Nieruchomości - Aneksy"
        ordering = ["contract_immovables", "date_annex"]

    contract_immovables = models.ForeignKey(ContractImmovables, on_delete=models.CASCADE,
                                            verbose_name="umowa",
                                            related_name="annex")
    scan_annex = models.FileField(upload_to=upload_scan_annex_contract_immovables, null=True, verbose_name="Skan aneks")
    date_annex = models.DateField("Data aneksu", null=True)
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_annex.strftime('%d.%m.%Y')} {self.scan_annex}"


def up_load_contract_auction(instance, filename):
    extension = filename.split(".")[-1]
    return f"contracts_zzp/{instance.no_contract}/Umowa_z_dnia_{instance.date.strftime('%d.%m.%Y')}.{extension}"


class ContractAuction(models.Model):
    class Meta:
        verbose_name = "Umowa ZZP"
        verbose_name_plural = "U.09 - Umowy ZZP"
        ordering = ["date"]

    investments_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True,
                                            related_name="contract_auction",
                                            verbose_name="Zadanie inwestycyjne")
    date = models.DateField("Data")
    no_contract = models.CharField("Nr. umowy", max_length=20, unique=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE,
                                   verbose_name="Kontrahent",
                                   related_name="contract_auction")
    price = models.DecimalField("Wartość umowy", max_digits=12, decimal_places=2)
    work_scope = models.CharField("Przedmiot umowy", max_length=120)
    legal_basic = models.ForeignKey(LegalBasic, on_delete=models.CASCADE, related_name="contract_auction",
                                    verbose_name="Tryb UPZP")
    end_date = models.DateField("Data zakończenia")

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Jednostka",
                             related_name="contract_auction")
    last_report_date = models.DateField("Data ostatniego protokołu", null=True, blank=True)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, verbose_name="Gwarancja",
                                  related_name="contract_auction", null=True, blank=True)
    guarantee_period = models.IntegerField(verbose_name="Okres gwarancji")
    warranty_period = models.IntegerField(verbose_name="Okres rękojmi")
    security_percent = models.DecimalField("Procent zabezpiecznia", max_digits=2, decimal_places=0, null=True,
                                           blank=True)
    security_sum = models.DecimalField("Kwota zabezpiecznia", max_digits=10, decimal_places=2, null=True,
                                       blank=True)
    worker = models.ManyToManyField(Employer, verbose_name="Inspektor", related_name="contract_auction")
    report = models.TextField("Raportowanie", blank=True, default="")
    information = models.TextField("Informacje", blank=True, default="")
    scan = models.FileField(upload_to=up_load_contract_auction, null=True, blank=True, verbose_name="Skan umowy")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiana", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="contract_auction",
                               verbose_name="Autor")

    def __str__(self):
        return f"{self.no_contract} z dnia {self.date.strftime('%d.%m.%Y')} r."


def up_load_annex_contract_auction(instance, filename):
    extension = filename.split(".")[-1]
    return f"contracts_zzp/{instance.contract_auction.no_contract}/Aneks_z_dnia_{instance.date.strftime('%d.%m.%Y')}.{extension}"


class AnnexContractAuction(models.Model):
    class Meta:
        verbose_name = "Aneks na umowę ZZP"
        verbose_name_plural = "U.10 - Umowy ZZP - Aneksy"
        ordering = ["contract_auction", "date"]

    contract_auction = models.ForeignKey(ContractAuction, on_delete=models.CASCADE,
                                         verbose_name="Umowa ZZP",
                                         related_name="aneks_contract_auction")
    date = models.DateField("Data aneksu")
    price_change = models.BooleanField("Zmiana wartości umowy", default=False)
    price_after_change = models.DecimalField("Kwota aneksu", max_digits=10, decimal_places=2, null=True, blank=True)
    scope_changes = models.TextField("Zakres zmian", blank=True, default="")
    scan = models.FileField(upload_to=up_load_annex_contract_auction, null=True, blank=True,
                            verbose_name="Skan aneksu")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor",
                               related_name="annexcontractauction")

    def __str__(self):
        return f"Aneks z dnia {self.date}"


class GuaranteeSettlement(models.Model):
    class Meta:
        verbose_name = "Rozliczenie umowy"
        verbose_name_plural = "U.11 - Umowy ZZP - Rozliczenia umów: Gwarancje"
        ordering = ["deadline_settlement"]

    contract = models.ForeignKey(ContractAuction, on_delete=models.CASCADE, verbose_name="Umowa",
                                 related_name="guarantee_settlement")
    deadline_settlement = models.DateField("Termin zwrotu")
    settlement_sum = models.DecimalField("Kwota zwrotu", max_digits=8, decimal_places=2, null=True, blank=True)
    script = models.CharField(verbose_name="L.dz. Pisma", max_length=50, null=False)
    affirmation_settlement = models.BooleanField(verbose_name="Rozliczono", default=False)

    def __str__(self):
        return f"{self.script} - Rozliczenie umowy {self.contract}"


class MediaType(models.Model):
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "U.06 - Umowy Media - Rodzaje Mediów"
        ordering = ["type"]

    type = models.CharField("Media", max_length=25)
    folders_type = models.CharField("Nazwa folderu", max_length=30)

    def __str__(self):
        return f"{self.type}"


def upload_contract_media(instance, filename):
    return f"contracts_media/{instance.type.folders_type}/{instance.contractor.name}/{filename}"


class ContractMedia(models.Model):
    class Meta:
        verbose_name = "Umowa na Media"
        verbose_name_plural = "U.04 - Umowy Media"
        ordering = ["-date"]

    date = models.DateField("Data umowy")
    no_contract = models.CharField("Nr.umowy", max_length=30)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Wykonawca",
                                   related_name="contract_media")
    type = models.ForeignKey(MediaType, on_delete=models.CASCADE, verbose_name="Rodzaj umowy",
                             related_name="contractmedia")
    legal_basic = models.ForeignKey(LegalBasic, on_delete=models.CASCADE, related_name="contract_media",
                                    verbose_name="Tryb UPZP")
    content = models.CharField("Treść", max_length=100)
    period_of_validity = models.DateField("Data obowiązywania", null=True, blank=True)
    unit = models.ManyToManyField(Unit, verbose_name="Jednostka", related_name="contract_media")
    contract_value = models.DecimalField(verbose_name="Wartośc umowy", decimal_places=2, max_digits=10, blank=True,
                                         null=True)
    information = models.TextField("Informacje", blank=True, default="")
    scan = models.FileField(upload_to=upload_contract_media, verbose_name="Skan", null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name="Branżysta",
                                 related_name="contract_media")
    state = models.BooleanField(default=True, verbose_name="Aktualna")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiany", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor",
                               related_name="contract_media")

    def __str__(self):
        return f"{self.no_contract} z dnia {self.date.strftime('%d.%m.%Y')}"


def upload_annex_contract_media(instance, filename):
    return f"contracts_media/{instance.contract_media.type.folders_type}/{instance.contract_media.contractor.name}/{filename}"


class AnnexContractMedia(models.Model):
    class Meta:
        verbose_name = "Aneks Umowy na media"
        verbose_name_plural = "U.05 - Umowy Media - Aneksy"
        ordering = ["contract_media", "date"]

    related_name = 'annex_contract_media'

    contract_media = models.ForeignKey(ContractMedia, on_delete=models.CASCADE, verbose_name="Umowa",
                                       related_name=related_name)
    date = models.DateField("Data aneksu")
    scope_changes = models.TextField("Zakres zmian", blank=True, default="")
    scan = models.FileField(upload_to=upload_annex_contract_media, null=True, blank=True, verbose_name="Skan aneksu")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor",
                               related_name=related_name)

    def __str__(self):
        return f"Aneks z dnia {self.date.strftime('%d.%m.%Y')}"


class UnitMeasure(models.Model):
    class Meta:
        verbose_name = "Jednostka miary"
        verbose_name_plural = "U.08 - Jednostki miary"
        ordering = ["id"]

    measureName = models.CharField("Jednostka miary", max_length=30)

    def __str__(self):
        return f'{self.measureName}'


class FinancialDocument(models.Model):
    class Meta:
        verbose_name = "Dokument księgowy"
        verbose_name_plural = "U.07 - Dokumenty księkowe"
        ordering = ["-date"]

    related_name = "financialdocument"

    contract = models.ForeignKey(ContractMedia, on_delete=models.CASCADE, verbose_name="Uowa",
                                 related_name=related_name)
    date = models.DateField("Data", null=False)
    no_document = models.CharField("Nr. dokumentu", max_length=30, null=False)
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE, verbose_name="Jednostka miary",
                                     related_name=related_name)
    value = models.DecimalField("Zużycie", max_digits=10, decimal_places=0)
    vat = models.ForeignKey(Tax, on_delete=models.CASCADE, verbose_name="Vat", related_name=related_name)
    cost_netto = models.DecimalField("Kwota netto", max_digits=10, decimal_places=2)
    cost_brutto = models.DecimalField("Kwota brutto", max_digits=10, decimal_places=2, null=True, blank=True)
    information = models.TextField("Informacje", null=True, blank=True, default="")
    creation_date = models.DateTimeField("Data utworzenia", auto_now_add=True)
    change = models.DateTimeField("Zmiany", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor",
                               related_name=related_name)

    def __str__(self):
        return f"{self.no_document} z dnia {self.date.strftime('%d.%m.%Y')}"
