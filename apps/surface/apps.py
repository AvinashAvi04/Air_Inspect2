from django.apps import AppConfig


class SurfaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.surface"

    def ready(self):
        import apps.surface.signals
