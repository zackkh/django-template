from allauth.account.signals import user_logged_in as allauth_user_logged_in

from accounts.mixins import AuthorMixin
from django.conf import settings
from django.contrib.auth.signals import user_logged_in as django_user_logged_in
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(AuthorMixin):
    MESSAGE_SERIALIZER = (
        "accounts.consumers.serializers.NotificationSerializer"
    )
    VIEWSET_READONLY = True

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    INFO, WARNING, DANGER = "Information", "Warning", "Danger"
    LEVEL_CHOICES = (
        (INFO, INFO),
        (WARNING, WARNING),
        (DANGER, DANGER),
    )

    title = models.TextField(_("title"))
    level = models.CharField(
        _("level"), choices=LEVEL_CHOICES, default=INFO, max_length=255
    )
    content = models.TextField(_("content"))

    added_on = models.DateTimeField(_("added on"), auto_now_add=True)
    modified_on = models.DateTimeField(_("modified on"), auto_now=True)


class Device(AuthorMixin):
    class Meta:
        verbose_name = _("device")
        verbose_name_plural = _("devices")

    user_agent = models.TextField(_("user agent"), blank=True, null=True)
    ip_address = models.GenericIPAddressField(
        _("ip address"), blank=True, null=True, unpack_ipv4=True
    )

    added_on = models.DateTimeField(_("added on"), auto_now_add=True)
    modified_on = models.DateTimeField(_("modified on"), auto_now=True)


NEW_DEVICE_CONTENT = """
A new sign-in has been detected:

User-agent: {user_agent}
IP: {ip_address}

You can ignore this email if it was you;
If not, reset your password now.
"""


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def save_user_agent_data(sender, request, user, **kwargs):
    user_agent = request.META.get("HTTP_USER_AGENT")
    # Use REMOTE_ADDR for the client's IP address
    ip_address = get_client_ip(request)

    if (
        user_agent
        and not user.device_set.filter(
            user_agent=user_agent, ip_address=ip_address
        ).exists()
    ):
        user.email_user(
            subject="New device detected!",
            message=NEW_DEVICE_CONTENT.format(
                user_agent=user_agent, ip_address=ip_address
            ),
            from_email=getattr(settings, "EMAIL_HOST_USER", "admin@localhost"),
        )
        user.device_set.create(user_agent=user_agent, ip_address=ip_address)


allauth_user_logged_in.connect(save_user_agent_data)
django_user_logged_in.connect(save_user_agent_data)
