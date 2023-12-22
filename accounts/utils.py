from crum import get_current_request

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


def get_user(pk):
    User = get_user_model()

    try:
        return User._default_manager.get(pk=pk)
    except ObjectDoesNotExist:
        return None


def get_watcher_user(as_user=False):
    User = get_user_model()

    watcher, created = User._default_manager.get_or_create(
        username="watcher",
        first_name="Watcher",
        last_name="User",
        is_active=False,
        is_superuser=True,
        is_staff=True,
    )

    return watcher if as_user else watcher.pk


def get_deleted_user(as_user=False):
    User = get_user_model()

    deleted, created = User._default_manager.get_or_create(
        username="deleted",
        first_name="Deleted",
        last_name="User",
        is_active=False,
        is_superuser=True,
        is_staff=True,
    )

    return deleted if as_user else deleted.pk


def get_current_or_watcher_user(as_user=False):
    request = get_current_request()

    if request:
        return request.user.pk

    return get_watcher_user()
