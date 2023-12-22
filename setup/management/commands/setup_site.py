import os

from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Set up current site in django's Admin panel."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        try:
            site = Site.objects.get_current()
        except Site.DoesNotExist:
            return

        site.domain = os.getenv("SITE_DOMAIN")
        site.name = os.getenv("SITE_NAME")

        site.save(update_fields=["domain", "name"])
