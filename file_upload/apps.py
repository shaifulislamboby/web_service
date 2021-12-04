from django.apps import AppConfig


class FileUploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file_upload'

    def ready(self):
        from .signals import handlers
