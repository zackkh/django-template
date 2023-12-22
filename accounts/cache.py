from django.conf import settings
from django.core.cache import cache


def make_cache_name(user):
    return f"cache-{user.pk}"


class UserCache:
    API_CACHE_NAME = "cache-%s"

    def __init__(self, user, cache_name=None):
        self.cache_name = (cache_name or self.API_CACHE_NAME) % user.username

    def get(self):
        return cache.get(self.cache_name)

    def set(self, data, timeout=None):
        if timeout is None:
            timeout = getattr(settings, "USER_CACHE_TIMEOUT", 60)

        cache.set(self.cache_name, data, timeout=timeout)

    def handle(self, data=None):
        current = self.get()
        if current:
            return current

        self.set(data)
        return data

    def clear(self):
        self.set(data=None)


def get_cache(user, cache_name=None):
    return UserCache(user=user, cache_name=cache_name)
