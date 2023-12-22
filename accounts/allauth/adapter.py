from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def get_email_confirmation_url(self, request, emailconfirmation):
        # Replace 'https://localhost:3000' with your actual frontend URL
        return "{domain}/auth/verify-email/?key={key}".format(
            domain=settings.FRONTEND_URL, key=emailconfirmation.key
        )


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        # Replace 'https://localhost:3000' with your actual frontend URL
        return "{domain}/auth/verify-email/?key={key}".format(
            domain=settings.FRONTEND_URL, key=emailconfirmation.key
        )
