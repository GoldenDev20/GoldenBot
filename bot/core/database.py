# bot/core/database.py

from motor.motor_asyncio import AsyncIOMotorClient

class DatabaseService:
    def __init__(self, uri, db_name):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def get_guild_config(self, guild_id: int):
        return await self.db.guilds.find_one({"guild_id": guild_id})

    async def update_guild_config(self, guild_id: int, data: dict):
        return await self.db.guilds.update_one(
            {"guild_id": guild_id}, {"$set": data}, upsert=True
        )
