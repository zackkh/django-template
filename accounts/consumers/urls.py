from accounts.consumers.consumer import NotificationConsumer
from django.urls import path

urlpatterns = [path("notifications/", NotificationConsumer.as_asgi())]
