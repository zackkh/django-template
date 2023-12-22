from accounts.models import Device, Notification, UserModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


# Register your models here.
@admin.register(UserModel)
class UserAdmin(AuthUserAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["user_agent", "ip_address", "author", "added_on"]
    search_fields = ["user_agent", "ip_address"]

    list_filter = ["author"]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "level", "author", "added_on"]
    search_fields = ["title"]

    list_filter = ["level", "author"]
