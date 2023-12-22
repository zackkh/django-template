from allauth.account.utils import user_pk_to_url_str
from allauth.utils import build_absolute_uri
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.serializers import PasswordResetSerializer

from django.conf import settings
from django.urls.base import reverse


def default_url_generator(request, user, temp_key):
    path = getattr(settings, "ACCOUNT_PASSWORD_RESET_CONFIRM", None)
    if path is None:
        path = reverse(
            "password_reset_confirm",
            args=[user_pk_to_url_str(user), temp_key],
        )
        if api_settings.PASSWORD_RESET_USE_SITES_DOMAIN:
            url = build_absolute_uri(None, path)
        else:
            url = build_absolute_uri(request, path)

        url = url.replace("%3F", "?")

        return url

    return path.format(uid=user_pk_to_url_str(user), token=temp_key)


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        return {"url_generator": default_url_generator}
