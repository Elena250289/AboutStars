from django.apps import AppConfig

# Отображение заголовка women-приложения 
class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
    verbose_name = 'Известные женщины'
