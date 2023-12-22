from django.urls import path

from accounts.api import views

urlpatterns = [
    path(
        "login/auth-google/",
        views.AuthorizationCodeGrantGoogleLogin.as_view(),
        name="auth-google_login",
    ),
    path(
        "login/imp-google/",
        views.ImplicitGrantGoogleLogin.as_view(),
        name="imp-google_login",
    ),
]
