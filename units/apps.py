from django.apps import AppConfig


class UnitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'units'
    verbose_name = "2. Jednostki Policji"

    def ready(self):
        import units.signals