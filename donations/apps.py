from django.apps import AppConfig


class DonationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donations'
    verbose_name = 'M.05 - Darowizny'

    def ready(self):
        import donations.signals
