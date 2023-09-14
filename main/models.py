from django.db import models
from enum import Enum
import os


# Create your models here.
class Team(models.Model):
    class Meta:
        verbose_name = "Komórka Wydziału"
        verbose_name_plural = "S.02 - Komórki Wydziału"
        ordering = ["priority"]

    priority = models.IntegerField("Priorytet", null=True, blank=True, default=0)
    team = models.CharField(max_length=50, verbose_name="Komórka Wydziału")
    active = models.BooleanField("Aktywny", default=True)

    def __str__(self):
        return f"{self.team}"


class TeamEnum(Enum):
    NK = [1, "Naczelnicy"]
    ZOK = [2, "Zespół Kancelaryjny"]
    ZRIWT = [3, "Zespół Rozliczen i Wsparcia technicznego"]
    ZI = [4, "Zespół Inwestychi"]
    ZE = [5, "Zespół Eksploatacji"]
    ZM = [6, "Zespół Mieszkaniowy"]
    ZN = [7, "Zespół Nieruchomości"]


class SecretariatTelephone(models.Model):
    class Meta:
        verbose_name = "Telefon do sekretariatu"
        verbose_name_plural = "S.05 - Telefony do sekretariatu"

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
        verbose_name_plural = "S.06 - Książka telefoniczna KWP w Poznaniu"

    telephone_book = models.FileField(upload_to="KWP_telephone/%Y/", null=True,
                                      verbose_name="Spis telefonów KWP w Poznaniu")
    add_date = models.DateField("Data dodania", auto_now_add=True)


class IndustryType(models.Model):
    class Meta:
        verbose_name = "Branża"
        verbose_name_plural = "S.03 - Branże"

    industry = models.CharField("Brażna", max_length=50)

    def __str__(self):
        return f"{self.industry}"


class Employer(models.Model):
    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "S.04 - Pracownicy"
        ordering = ["team", "last_name"]

    related_name = "employer"

    id_swop = models.CharField(verbose_name="ID SWOP", max_length=6, unique=True)
    name = models.CharField(verbose_name="Imię", max_length=20)
    last_name = models.CharField(verbose_name="Nazwisko", max_length=25)
    position = models.CharField(verbose_name="Stanowisko", max_length=20, blank=True, default="")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Zespół", related_name=related_name)
    industry_specialist = models.BooleanField(default=False, verbose_name="Branżysta")
    invoices_issues = models.BooleanField(default=False, verbose_name="Wystawianie faktur")
    industry = models.ForeignKey(IndustryType, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Branża",
                                 related_name=related_name)
    no_room = models.CharField(verbose_name="Nr. pokoju", max_length=2, blank=True, default="")
    no_tel_room = models.CharField(verbose_name="Nr. telefonu", max_length=6, blank=True, default="")
    no_tel_private = models.CharField(verbose_name="Nr. komórkowy", max_length=9, blank=True, default="")
    information = models.TextField(verbose_name="Informacje", max_length=200, null=True, blank=True)
    deleted = models.BooleanField(verbose_name="Usunięty", default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField(verbose_name="Data zmian", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, related_name="employer")

    def __str__(self):
        return f"{self.name} {self.last_name}"


class AccessModule(models.Model):
    relatedName = "accessmodule"

    class Meta:
        verbose_name = "Dostęp do modułów"
        verbose_name_plural = "S.01 - Dostęp do modułów"

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, verbose_name="Użytkownik",
                                related_name=relatedName)
    zok_team = models.BooleanField(verbose_name="Ewidencja: Zespoł Obsługi Kancelarynej", default=False)
    teams = models.BooleanField(verbose_name="ZOK - Zespoły", default=False)
    commands = models.BooleanField(verbose_name="ZOK - Polecenia", default=False)
    employers = models.BooleanField(verbose_name="ZOK - Pracownicy", default=False)
    cars = models.BooleanField(verbose_name="ZOK - Rezerwacja samochodu służbowego", default=False)
    zriwt_team = models.BooleanField(verbose_name="Ewidencja: Zespół Rozliczeń i Wsparcia Technicznego", default=False)
    contractors_module = models.BooleanField(verbose_name="ZRiWT - Kontrahenci - Podgląd", default=False)
    contractors_module_edit = models.BooleanField(verbose_name="ZRiWT - Kontrahenci - Edycja", default=False)
    invoices_module = models.BooleanField(verbose_name="ZRiWT - Faktury - Podgląd", default=False)
    invoices_module_edit = models.BooleanField(verbose_name="ZRiWT - Faktury - Edycja", default=False)
    donations_module = models.BooleanField(verbose_name="ZRiWT - Darowizny - Podgląd", default=False)
    donations_module_edit = models.BooleanField(verbose_name="ZRiWT - Darowizny - Edycja", default=False)
    buildings_module = models.BooleanField(verbose_name="ZRiWT - Środki trwałe - budynki - Podgląd", default=False)
    buildings_module_edit = models.BooleanField(verbose_name="ZRiWT - Środki trwałe - budynki - Edycja", default=False)
    inspections_module = models.BooleanField(verbose_name="ZRiWT - Przeglądy - Podgląd", default=False)
    inspections_module_edit = models.BooleanField(verbose_name="ZRiWT - Przeglądy - Edycja", default=False)
    contracts_auction_module = models.BooleanField(verbose_name="ZRiWT - Umowy ZZP - Podgląd", default=False)
    contracts_auction_module_edit = models.BooleanField(verbose_name="ZRiWT - Umowy ZZP - Edycja", default=False)
    investments_module = models.BooleanField(verbose_name="ZRiWT - Inwestycje - Podgląd", default=False)
    investments_module_edit = models.BooleanField(verbose_name="ZRiWT - Inwestycje - Edycja", default=False)
    cpvdict_module = models.BooleanField(verbose_name="ZRiWT - Rodzajowość - Podgląd", default=False)
    cpvdict_module_edit = models.BooleanField(verbose_name="ZRiWT - Rodzajowość - Edycja", default=False)
    gallery_module = models.BooleanField(verbose_name="ZRiWT - Galeria - Podgląd", default=False)
    gallery_module_edit = models.BooleanField(verbose_name="ZRiWT - Galeria - Edycja", default=False)
    zm_team = models.BooleanField(verbose_name="Ewidencja: Zespół Mieszkaniowy", default=False)
    official_flat = models.BooleanField(verbose_name="ZM - Mieszkania służbowe - Podgląd", default=False)
    official_flat_edit = models.BooleanField(verbose_name="ZM - Mieszkania służbowe - Edycja", default=False)
    zn_team = models.BooleanField(verbose_name="Ewidencja: Zespół Nieruchomości", default=False)
    units = models.BooleanField(verbose_name="ZN - Jednostki - Podgląd", default=False)
    units_edit = models.BooleanField(verbose_name="ZN - Jednostki - Edycja", default=False)
    contract_immovables = models.BooleanField(verbose_name="ZN - Umowy nieruchomości - Podgląd", default=False)
    contract_immovables_edit = models.BooleanField(verbose_name="ZN - Umowy nieruchomości - Edycja", default=False)
    ze_team = models.BooleanField(verbose_name="Ewidencja: Zespół Eksploatacji", default=False)
    records_letters = models.BooleanField(verbose_name="ZE - Ewidencja Pism - Podgląd", default=False)
    records_letters_edit = models.BooleanField(verbose_name="ZE - Ewidencja Pism - Edycja", default=False)
    contract_media = models.BooleanField(verbose_name="ZE - Umowy Media - Podgląd", default=False)
    contract_media_edit = models.BooleanField(verbose_name="ZE - Umowy Media - Edycja", default=False)

    def __str__(self):
        return f"{self.user} - {self.user.first_name} {self.user.last_name}"


def upload_scan(instance, filename):
    extension = filename.split(".")[-1]
    title = instance.title
    new_title = title.replace(" ", "_")
    return f"commands/{new_title}.{extension}"


class Command(models.Model):
    class Meta:
        verbose_name = "Polecenie"
        verbose_name_plural = "S.07 - Polecenia"
        ordering = ["-create_date"]

    title = models.CharField("Nazwa", max_length=120)
    content = models.TextField("Treść")
    scan = models.FileField(upload_to=upload_scan, verbose_name="Skan polecenia")
    change = models.DateTimeField(verbose_name="Data zmian", auto_now=True)
    create_date = models.DateTimeField(verbose_name="Data dodania", auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Car(models.Model):
    class Meta:
        verbose_name = "Samochód sużbowy"
        verbose_name_plural = "S.08 - Samochód służbowy"
        ordering = ["-rent_date"]

    related_name = "car"

    rent_date = models.DateField(verbose_name="Data", unique=True)
    borrower = models.ManyToManyField(Employer, verbose_name="Delegat", related_name=related_name)
    target = models.TextField("Cel")
    create_date = models.DateTimeField(verbose_name="Data utworzenia", auto_now_add=True)
    change = models.DateTimeField(verbose_name="Zmiana", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, related_name=related_name, verbose_name="Autor")

    def __str__(self):
        return f"{self.rent_date.strftime('%d.%m.%Y')} - {self.target}"


def upload_file(instance, filename):
    extension = filename.split(".")[-1]
    title = instance.title
    new_title = title.replace(" ", "_")
    return f'shared_file/{new_title}.{extension}'


class NecesseryFile(models.Model):
    class Meta:
        verbose_name = 'Plik'
        verbose_name_plural = 'S.09 - Pliki do pobrania'
        ordering = ['-create_date']

    related_name = 'necessery_files'

    title = models.CharField(verbose_name='Nazwa pliku', max_length=300)
    file = models.FileField(upload_to=upload_file, null=False, verbose_name="Plik")
    create_date = models.DateTimeField(verbose_name="Data utworzenia", auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
