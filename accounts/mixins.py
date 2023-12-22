from accounts.utils import get_current_or_watcher_user, get_deleted_user
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthorMixin(models.Model):
    class Meta:
        abstract = True

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("author"),
        blank=True,
        null=True,
        editable=False,
        default=get_current_or_watcher_user,
        on_delete=models.SET(get_deleted_user),
    )


class UserMixin(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        blank=True,
        null=True,
        on_delete=models.SET(get_deleted_user),
    )
