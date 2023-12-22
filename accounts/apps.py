from accounts.pg import (
    prevent_server_users_deletion_trigger,
    prevent_server_users_update_trigger,
)
from django.apps import AppConfig
from django.db import models


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self) -> None:
        try:
            from accounts import signals  # noqa
        except ImportError:
            pass

        models.signals.post_migrate.connect(
            prevent_server_users_deletion_trigger, sender=self
        )

        models.signals.post_migrate.connect(
            prevent_server_users_update_trigger, sender=self
        )
        return super().ready()
