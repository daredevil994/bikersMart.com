from django.apps import AppConfig


class MyprofileappConfig(AppConfig):
    name = 'myProfileApp'

    def ready(self):
        import users.signals
