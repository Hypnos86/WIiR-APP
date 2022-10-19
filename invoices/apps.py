from django.apps import AppConfig


class InvoicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invoices'
    verbose_name = "M.07 - Faktury"

    def ready(self):
        import invoices.signals