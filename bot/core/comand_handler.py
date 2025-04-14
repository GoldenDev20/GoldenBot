# bot/core/command_handler.py

from discord.ext import commands

class CommandHandler:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def register_commands(self):
        # Here you'd load Cogs or define slash commands
        from bot.commands import general  # example
        self.bot.add_cog(general.General(self.bot))

    def setup(self):
        self.register_commands()
