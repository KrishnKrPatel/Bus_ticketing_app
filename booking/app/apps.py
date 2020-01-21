from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfig):
    name = 'app'
    verbose_name = _('profiles')

    def ready(self):
        import app.signals  # noqa
