from django.apps import AppConfig


class DocstoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "docstore"

    def ready(self):
        import docstore.signals  # NoQa
