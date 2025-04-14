# bot/core/cache.py

import aioredis

class CacheManager:
    def __init__(self, redis_url):
        self.redis_url = redis_url
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(self.redis_url)

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value, expire=None):
        await self.redis.set(key, value, ex=expire)
