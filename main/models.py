from django.db import models
import os


# Create your models here.
class Team(models.Model):
    class Meta:
        verbose_name = "Komórka Wydziału"
        verbose_name_plural = "Komórki Wydziału"
        ordering = ["priority"]

    priority = models.IntegerField("Priorytet", null=True, blank=True, default=0)
    team = models.CharField(max_length=50, verbose_name="Komórka Wydziału")
    active = models.BooleanField("Aktywny")

    def __str__(self):
        return f"{self.team}"


class SecretariatTelephone(models.Model):
    class Meta:
        verbose_name = "Telefon do sekretariatu"
        verbose_name_plural = "Telefony do sekretariatu"

    code = models.IntegerField("Nr. kierunkowy", null=True, blank=True)
    fax_number = models.CharField("Nr. faxu", max_length=6, null=True, blank=True, default="")
    secretariat_number = models.CharField("Nr. do sekretariatu", max_length=6, null=True, blank=True, default="")
    information = models.TextField("Informacje", null=True, blank=True)
    create = models.DateTimeField("Data utworzenia", auto_now_add=True)

    def __str__(self):
        return f"{self.code} {self.secretariat_number}"


class OrganisationTelephone(models.Model):
    class Meta:
        verbose_name = "Książka telefoniczna KWP w Poznaniu"
        verbose_name_plural = "Książka telefoniczna KWP w Poznaniu"

    telephone_book = models.FileField(upload_to="KWP_telephone/%Y/", null=True,
                                      verbose_name="Spis telefonów KWP w Poznaniu")
    add_date = models.DateField("Data dodania", auto_now_add=True)


class IndustryType(models.Model):
    class Meta:
        verbose_name = "Branża"
        verbose_name_plural = "Branże"

    industry = models.CharField("Brażna", max_length=50)

    def __str__(self):
        return f"{self.industry}"


class Employer(models.Model):
    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"
        ordering = ["team", "last_name"]

    id_swop = models.CharField("ID SWOP", max_length=6, unique=True)
    name = models.CharField("Imię", max_length=20)
    last_name = models.CharField("Nazwisko", max_length=25)
    position = models.CharField("Stanowisko", max_length=20, blank=True, default="")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Zespół", related_name="employer")
    industry_specialist = models.BooleanField(default=False, verbose_name="Branżysta")
    invoices_issues = models.BooleanField(default=False, verbose_name="Wystawianie faktur")
    industry = models.ForeignKey(IndustryType, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Branża",
                                 related_name="employer")
    no_room = models.CharField("Nr. pokoju", max_length=2, blank=True, default="")
    no_tel_room = models.CharField("Nr. telefonu", max_length=6, blank=True, default="")
    no_tel_private = models.CharField("Nr. komórkowy", max_length=9, blank=True, default="")
    information = models.TextField("Informacje", max_length=200, null=True, blank=True)
    deleted = models.BooleanField("Usunięty", default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField("Data zmian", auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="employer")

    def __str__(self):
        return f"{self.name} {self.last_name}"


class AccessModule(models.Model):
    relatedName = "accessmodule"
    class Meta:
        verbose_name = "Dostęp do modułów"
        verbose_name_plural = "Dostęp do modułów"

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, verbose_name="Użytkownik",
                                related_name=relatedName)
    zok_team = models.BooleanField("Ewidencja: Zespoł Obsługi Kancelarynej", default=False)
    teams = models.BooleanField("ZOK - Zespoły", default=False)
    commands = models.BooleanField("ZOK - Polecenia", default=False)
    employers = models.BooleanField("ZOK - Pracownicy", default=False)
    zriwt_team = models.BooleanField("Ewidencja: Zespół Rozliczeń i Wsparcia Technicznego", default=False)
    contractors_module = models.BooleanField("ZRiWT - Kontrahenci - Podgląd", default=False)
    contractors_module_edit = models.BooleanField("ZRiWT - Kontrahenci - Edycja", default=False)
    invoices_module = models.BooleanField("ZRiWT - Faktury - Podgląd", default=False)
    invoices_module_edit = models.BooleanField("ZRiWT - Faktury - Edycja", default=False)
    donations_module = models.BooleanField("ZRiWT - Darowizny - Podgląd", default=False)
    donations_module_edit = models.BooleanField("ZRiWT - Darowizny - Edycja", default=False)
    buildings_module = models.BooleanField("ZRiWT - Środki trwałe - budynki - Podgląd", default=False)
    buildings_module_edit = models.BooleanField("ZRiWT - Środki trwałe - budynki - Edycja", default=False)
    inspections_module = models.BooleanField("ZRiWT - Przeglądy - Podgląd", default=False)
    inspections_module_edit = models.BooleanField("ZRiWT - Przeglądy - Edycja", default=False)
    contracts_auction_module = models.BooleanField("ZRiWT - Umowy ZZP - Podgląd", default=False)
    contracts_auction_module_edit = models.BooleanField("ZRiWT - Umowy ZZP - Edycja", default=False)
    investments_module = models.BooleanField("ZRiWT - Inwestycje - Podgląd", default=False)
    investments_module_edit = models.BooleanField("ZRiWT - Inwestycje - Edycja", default=False)
    cpvdict_module = models.BooleanField("ZRiWT - Rodzajowość - Podgląd", default=False)
    cpvdict_module_edit = models.BooleanField("ZRiWT - Rodzajowość - Edycja", default=False)
    gallery_module = models.BooleanField("ZRiWT - Galeria - Podgląd", default=False)
    gallery_module_edit = models.BooleanField("ZRiWT - Galeria - Edycja", default=False)
    zm_team = models.BooleanField("Ewidencja: Zespół Mieszkaniowy", default=False)
    official_flat = models.BooleanField("ZM - Mieszkania służbowe - Podgląd", default=False)
    official_flat_edit = models.BooleanField("ZM - Mieszkania służbowe - Edycja", default=False)
    zn_team = models.BooleanField("Ewidencja: Zespół Nieruchomości", default=False)
    units = models.BooleanField("ZN - Jednostki - Podgląd", default=False)
    units_edit = models.BooleanField("ZN - Jednostki - Edycja", default=False)
    contract_immovables = models.BooleanField("ZN - Umowy nieruchomości - Podgląd", default=False)
    contract_immovables_edit = models.BooleanField("ZN - Umowy nieruchomości - Edycja", default=False)
    ze_team = models.BooleanField("Ewidencja: Zespół Eksploatacji", default=False)
    contract_media = models.BooleanField("ZE - Umowy Media - Podgląd", default=False)
    contract_media_edit = models.BooleanField("ZE - Umowy Media - Edycja", default=False)

    def __str__(self):
        return f"{self.user}"


def upload_scan(instance, filename):
    extension = os.path.splitext(filename)[1]
    name_file = f"{instance.title}{extension}"
    return f"commands/{name_file}"


class Command(models.Model):
    class Meta:
        verbose_name = "Polecenie"
        verbose_name_plural = "Polecenia"
        ordering = ["create_date"]

    title = models.CharField("Nazwa", max_length=120)
    content = models.TextField("Treść")
    scan = models.FileField(upload_to=upload_scan, verbose_name="Skan polecenia")
    change = models.DateTimeField("Data zmian", auto_now=True)
    create_date = models.DateField("Data dodania", auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
