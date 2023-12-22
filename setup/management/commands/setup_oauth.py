import json

from allauth.socialaccount.models import SocialApp

from django.contrib.sites.models import Site
from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)
from django.db import transaction


class Command(BaseCommand):
    help = "django command to setup oauth app for django-allauth."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--path",
            default=None,
            help="Path of json file holding oauth config",
        )
        return super().add_arguments(parser)

    @transaction.atomic
    def handle(self, *args, **kwargs):
        try:
            site = Site.objects.get_current()
        except Site.DoesNotExist as e:
            raise CommandError(str(e))

        path = kwargs.get("path", None)
        if path is None:
            raise CommandError(
                "You must provide a path of oauth config json file."
            )

        configs = json.loads(open(path, "r"))

        for config in configs:
            app, _ = SocialApp.objects.get_or_create(
                provider=config["github"],
                name=config["name"],
                client_id=config["client_id"],
                secret=config["secret"],
            )

            app.client_id = config["client_id"]
            app.secret = config["secret"]
            app.save(update_fields=["client_id", "secret"])

            # Add current site to app
            app.sites.add(site)
