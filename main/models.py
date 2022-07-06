from django.db import models


# Create your models here.
class Team(models.Model):
    class Meta:
        verbose_name = "Komórka Wydziału"
        verbose_name_plural = "Komórki Wydziału"
        ordering = ['priority']

    priority = models.IntegerField('Priorytet', null=True, blank=True, default=0)
    team = models.CharField(max_length=50, verbose_name='Komórka Wydziału')
    active = models.BooleanField('Aktywny')

    def __str__(self):
        return f'{self.team}'


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
    position = models.CharField("Stanowisko", max_length=20, blank=True, default="")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Zespół', related_name='employer')
    industry_specialist = models.BooleanField(default=0, verbose_name='Branżysta merytoryczny')
    industry = models.ForeignKey(IndustryType, on_delete=models.CASCADE, null=True,blank=True,  verbose_name='Branża', related_name='employer')
    no_room = models.CharField("Nr. pokoju", max_length=2, blank=True, default="")
    no_tel_room = models.CharField("Nr. telefonu", max_length=6, blank=True, default="")
    no_tel_private = models.CharField("Nr. komórkowy", max_length=9, blank=True, default="")
    information = models.TextField("Informacje", max_length=200, null=True, blank=True)
    deleted = models.BooleanField('Usunięty', default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField('Zmiany', auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='employer')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class AccessModule(models.Model):
    class Meta:
        verbose_name = 'Dostęp do modułów'
        verbose_name_plural = 'Dostęp do modułów'

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='Użytkownik',
                                related_name='accessmodule')
    zok_team = models.BooleanField('Ewidencja: Zespoł Obsługi Kancelarynej', default=False)
    commands = models.BooleanField('ZOK - Polecenia', default=False)
    zriwt_team = models.BooleanField('Ewidencja: Zespół Rozliczeń i Wsparcia Technicznego', default=False)
    contractors_module = models.BooleanField('ZRiWT - Kontrahenci - Podgląd', default=False)
    contractors_module_edit = models.BooleanField('ZRiWT - Kontrahenci - Edycja', default=False)
    invoices_module = models.BooleanField('ZRiWT - Faktury - Podgląd', default=False)
    invoices_module_edit = models.BooleanField('ZRiWT - Faktury - Edycja', default=False)
    donations_module = models.BooleanField('ZRiWT - Darowizny - Podgląd', default=False)
    donations_module_edit = models.BooleanField('ZRiWT - Darowizny - Edycja', default=False)
    contracts_auction_module = models.BooleanField('ZRiWT - Umowy ZZP - Podgląd', default=False)
    contracts_auction_module_edit = models.BooleanField('ZRiWT - Umowy ZZP - Edycja', default=False)
    investments_module = models.BooleanField('ZRiWT - Inwestycje - Podgląd', default=False)
    investments_module_edit = models.BooleanField('ZRiWT - Inwestycje - Edycja', default=False)
    cpvdict_module = models.BooleanField('ZRiWT - Rodzajowość - Podgląd', default=False)
    cpvdict_module_edit = models.BooleanField('ZRiWT - Rodzajowość - Edycja', default=False)
    gallery_module = models.BooleanField('ZRiWT - Galeria - Podgląd', default=False)
    gallery_module_edit = models.BooleanField('ZRiWT - Galeria - Edycja', default=False)
    zm_team = models.BooleanField('Ewidencja: Zespół Mieszkaniowy', default=False)
    official_flat = models.BooleanField('ZM - Mieszkania służbowe - Podgląd', default=False)
    official_flat_edit = models.BooleanField('ZM - Mieszkania służbowe - Edycja', default=False)
    zn_team = models.BooleanField('Ewidencja: Zespół Nieruchomości', default=False)
    contract_immovables = models.BooleanField('ZN - Umowy nieruchomości - Podgląd', default=False)
    contract_immovables_edit = models.BooleanField('ZN - Umowy nieruchomości - Edycja', default=False)
    ze_team = models.BooleanField('Ewidencja: Zespół Eksploatacji', default=False)

    def __str__(self):
        return f'{self.user}'


class Command(models.Model):
    class Meta:
        verbose_name = 'Polecenie'
        verbose_name_plural = 'Polecenia'
        ordering = ['create_date']

    title = models.CharField('Nazwa', max_length=120)
    content = models.TextField('Treść')
    scan = models.FileField(upload_to='commands/%Y/', verbose_name='Skan polecenia')
    create_date = models.DateField("Data dodania", auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
