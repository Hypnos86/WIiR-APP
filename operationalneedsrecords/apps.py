from django.apps import AppConfig


class OperationalneedsrecordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'operationalneedsrecords'
    verbose_name = 'M.12 - Eksploatacja'

    def ready(self):
        import operationalneedsrecords.signals
