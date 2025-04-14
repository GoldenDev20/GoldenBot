# bot/core/event_dispatcher.py

class EventDispatcher:
    def __init__(self, bot):
        self.bot = bot

    def bind_events(self):
        @self.bot.event
        async def on_ready():
            print(f"Logged in as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            # Important: Allow commands to still work
            await self.bot.process_commands(message)
