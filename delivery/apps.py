# from django.apps import AppConfig


# class DeliveryConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'delivery'



from django.apps import AppConfig

class DeliveryConfig(AppConfig):
    name = 'delivery'

    def ready(self):
        import delivery.signals  
