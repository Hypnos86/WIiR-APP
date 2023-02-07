from django.apps import AppConfig


class ConstructioninspectionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'constructioninspections'
    verbose_name = "M.11 - Przeglądy"

    def ready(self):
        import constructioninspections.signals
