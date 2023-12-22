from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = "Create admin user to access the Admin panel."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        if not settings.DEBUG:
            raise CommandError(
                "Command `create_admin` is only available during development."
            )

        data = dict(
            username="admin",
            password="admin",
            is_superuser=True,
            is_active=True,
            is_staff=True,
        )
        if (
            not get_user_model()
            .objects.filter(username=data["username"])
            .exists()
        ):
            get_user_model().objects.create_superuser(**data)
