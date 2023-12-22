from accounts.models import Notification
from django.contrib.auth.password_validation import MinimumLengthValidator


class MyPasswordValidator(MinimumLengthValidator):
    def password_changed(self, password, user):
        Notification._default_manager.create(
            title="Password change detected!",
            level=Notification.DANGER,
            content="Your password has been changed.",
            user=user,
        )
