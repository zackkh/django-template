from django.conf import settings
from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def setup_server_post_migration(sender, **kwargs):
    if settings.DEBUG:
        call_command("create_admin")

    call_command("setup_site")
