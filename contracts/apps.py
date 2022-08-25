from django.apps import AppConfig


class ContractsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contracts'
    verbose_name = "M.04 - Umowy"

    def ready(self):
        import contracts.signals
