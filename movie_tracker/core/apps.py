from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_tracker.core'
    
    def ready(self):
        # import signal handlers to register login/logout messages
        try:
            from . import signals  # noqa: F401
        except Exception:
            pass
