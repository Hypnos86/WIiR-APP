from django.apps import AppConfig


class MainConfig(AppConfig):
    no = 1
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = f'{no}. Sekretariat - Główny Panel'