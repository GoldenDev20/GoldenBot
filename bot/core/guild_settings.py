# bot/core/guild_settings.py

class GuildSettingsService:
    def __init__(self, database_service):
        self.database = database_service

    async def get_settings(self, guild_id: int):
        return await self.database.get_guild_config(guild_id)

    async def update_settings(self, guild_id: int, data: dict):
        return await self.database.update_guild_config(guild_id, data)
