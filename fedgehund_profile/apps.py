from django.apps import AppConfig


class FedgehundProfileConfig(AppConfig):
    name = 'fedgehund_profile'

    def ready(self):
    	from fedgehund_profile import signals