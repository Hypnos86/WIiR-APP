from django.apps import AppConfig


class CpvdictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cpvdict'
    verbose_name = "M.08 - Rodzajowość WIiR"

    def ready(self):
        import cpvdict.signals
