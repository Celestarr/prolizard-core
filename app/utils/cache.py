import functools

from django.core.cache import cache
from django.core.cache.backends.redis import RedisCache as DjangoRedisCache
from redis import Redis
from redis.exceptions import LockError


class RedisCache(DjangoRedisCache):
    def lock(self, name: str, timeout: float):
        client: Redis = self._cache.get_client(write=True)
        return client.lock(name, blocking=False, timeout=timeout)


def redis_lock(name: str, timeout: float = 5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            lock = cache.lock(name, timeout)

            try:
                if not lock.acquire():
                    raise LockError(f"Unable to acquire lock '{name}'")

                result = func(*args, **kwargs)
                return result

            finally:
                try:
                    lock.release()
                except LockError:
                    pass  # Lock was already released or expired

        return wrapper

    return decorator
