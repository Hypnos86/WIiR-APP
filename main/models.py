from django.db import models


# Create your models here.
class Team(models.Model):
    class Meta:
        verbose_name = "Komórka Wydziału"
        verbose_name_plural = "Komórki Wydziału"

    team = models.CharField(max_length=50, verbose_name='Zespół')

    def __str__(self):
        return f'{self.team}'


class Telephone(models.Model):
    class Meta:
        verbose_name = "Telefony"
        verbose_name_plural = "Telefony"
        ordering = ['team', 'position']

    team = models.ForeignKey("main.Team", on_delete=models.CASCADE, verbose_name='Zespół')
    position = models.CharField("Stanowisko", max_length=20, blank=True, default="")
    fname = models.CharField("Imię", max_length=15, blank=True, default="")
    lname = models.CharField("Nazwisko", max_length=15, null=True, blank=True, default="")
    no_room = models.CharField("Nr. pokoju", max_length=2, blank=True, default="")
    no_tel_room = models.CharField("Nr. telefonu", max_length=6, blank=True, default="")
    no_tel_private = models.CharField("Nr. komórkowy", max_length=9, null=True, blank=True, default="")
    information = models.CharField("Informacje", max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.position}. Tel: {self.no_tel_room}'


class OrganisationTelephone(models.Model):
    class Meta:
        verbose_name = "Książka telefoniczna KWP w Poznaniu"
        verbose_name_plural = "Książka telefoniczna KWP w Poznaniu"

    telephone_book = models.FileField(upload_to='KWP_telephone/%Y/', null=True,
                                      verbose_name="Spis telefonów KWP w Poznaniu")
    add_date = models.DateField("Data dodania", auto_now_add=True)


class IndustryType(models.Model):
    class Meta:
        verbose_name = 'Branża'
        verbose_name_plural = 'Branże'

    industry = models.CharField('Brażna', max_length=50)

    def __str__(self):
        return f'{self.industry}'


class Employer(models.Model):
    class Meta:
        verbose_name = 'Pracownik'
        verbose_name_plural = 'Pracownicy'
        ordering = ['team', 'last_name']

    name = models.CharField('Imię', max_length=20)
    last_name = models.CharField('Nazwisko', max_length=25)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Zespół')
    industry_specialist = models.BooleanField(default=0, verbose_name='Branżysta merytoryczny')
    industry = models.ForeignKey(IndustryType, on_delete=models.CASCADE, verbose_name='Branża')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class AccessModule(models.Model):
    class Meta:
        verbose_name = 'Dostęp do modułów'
        verbose_name_plural = 'Dostęp do modułów'

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='Użytkownik',
                                related_name='accessmodule')
    zriwt_team = models.BooleanField('Ewidencja: Zespół Rozliczeń i Wsparcia Technicznego', default=False)
    contractors_module = models.BooleanField('ZRiWT - Kontrahenci - Podgląd', default=False)
    contractors_module_edit = models.BooleanField('ZRiWT - Kontrahenci - Edycja', default=False)
    invoices_module = models.BooleanField('ZRiWT - Faktury - Podgląd', default=False)
    invoices_module_edit = models.BooleanField('ZRiWT - Faktury - Edycja', default=False)
    donations_module = models.BooleanField('ZRiWT - Darowizny - Podgląd', default=False)
    donations_module_edit = models.BooleanField('ZRiWT - Darowizny - Edycja', default=False)
    contracts_auction_module = models.BooleanField('ZRiWT - Umowy ZZP - Podgląd', default=False)
    contracts_auction_module_edit = models.BooleanField('ZRiWT - Umowy ZZP - Edycja', default=False)
    zm_team = models.BooleanField('Ewidencja: Zespół Mieszkaniowy', default=False)
    official_flat = models.BooleanField('ZM - Mieszkania służbowe - Podgląd', default=False)
    official_flat_edit = models.BooleanField('ZM - Mieszkania służbowe - Edycja', default=False)
    ze_team = models.BooleanField('Ewidencja: Zespół Eksploatacji', default=False)
    zn_team = models.BooleanField('Ewidencja: Zespół Nieruchomości', default=False)
    contract_immovables = models.BooleanField('ZN - Umowy nieruchomości - Podgląd', default=False)
    contract_immovables_edit = models.BooleanField('ZN - Umowy nieruchomości - Edycja', default=False)
    investments_module = models.BooleanField('Inwestycje - Podgląd', default=False)
    investments_module_edit = models.BooleanField('Inwestycje - Edycja', default=False)
    cpvdict_module = models.BooleanField('Rodzajowość - Podgląd', default=False)
    cpvdict_module_edit = models.BooleanField('Rodzajowość - Edycja', default=False)
    gallery_module = models.BooleanField('Galeria - Podgląd', default=False)
    gallery_module_edit = models.BooleanField('Galeria - Edycja', default=False)

    def __str__(self):
        return f'{self.user}'


class Command(models.Model):
    class Meta:
        verbose_name = 'Polecenie'
        verbose_name_plural = 'Polecenia'
        ordering = ['create_date']

    title = models.CharField('Nazwa', max_length=120)
    content = models.TextField('Treść')
    scan = models.FileField(upload_to='commands/%Y/%m/', verbose_name='Skan polecenia')
    create_date = models.DateField("Data dodania", auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
