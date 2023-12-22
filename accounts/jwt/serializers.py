from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

# Get the UserModel
UserModel = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["name"] = user.name
        token["access_type"] = getattr(user, "access_type", None)

        return token


class RegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update(
            {
                "first_name": self.validated_data.get("first_name", ""),
                "last_name": self.validated_data.get("last_name", ""),
            }
        )
        return data


class MyUserDetailsSerializer(UserDetailsSerializer):
    access_type = serializers.ReadOnlyField(default=None)

    form_class = UserChangeForm

    class Meta:
        model = UserModel
        fields = (
            "id",
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "access_type",
        )
        read_only_fields = (
            "date_joined",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
        )
