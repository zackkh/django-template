from django.core.cache import caches
from django.test import TestCase


class TestCache(TestCase):
    def test_redis(self):
        # Check if the 'redis' cache is properly set up
        cache = caches["redis"]
        self.assertIsNotNone(cache)

        # Perform a simple operation to test the cache
        key = "test_key"
        value = "test_value"
        cache.set(key, value)
        cached_value = cache.get(key)
        self.assertEqual(cached_value, value)

    def test_memcached(self):
        # Check if the 'memcached' cache is properly set up
        cache = caches["memcached"]
        self.assertIsNotNone(cache)

        # Perform a simple operation to test the cache
        key = "test_key"
        value = "test_value"
        cache.set(key, value)
        cached_value = cache.get(key)
        self.assertEqual(cached_value, value)

    def test_database(self):
        # Check if the 'memcached' cache is properly set up
        cache = caches["database"]
        self.assertIsNotNone(cache)

        # Perform a simple operation to test the cache
        key = "test_key"
        value = "test_value"
        cache.set(key, value)
        cached_value = cache.get(key)
        self.assertEqual(cached_value, value)

    def test_filesystem(self):
        # Check if the 'memcached' cache is properly set up
        cache = caches["filesystem"]
        self.assertIsNotNone(cache)

        # Perform a simple operation to test the cache
        key = "test_key"
        value = "test_value"
        cache.set(key, value)
        cached_value = cache.get(key)
        self.assertEqual(cached_value, value)
