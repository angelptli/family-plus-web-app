from django.apps import AppConfig


class CustomUserModelConfig(AppConfig):
    """Configure the custom_user_model app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_user_model'
