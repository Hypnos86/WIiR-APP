from django.apps import AppConfig


class UnitsConfig(AppConfig):
    no = 2
    default_auto_field = 'django.db.models.BigAutoField'
    name = "units"
    verbose_name = f"{no}. Jednostki Policji"

    def ready(self):
        import units.signals