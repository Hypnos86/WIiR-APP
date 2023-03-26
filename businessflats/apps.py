from django.apps import AppConfig


class BusinessflatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'businessflats'
    verbose_name = 'M.09 - Mieszkania Służbowe'

    def ready(self):
        import businessflats.signals
