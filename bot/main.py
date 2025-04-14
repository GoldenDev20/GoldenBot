import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import structlog

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX", "!")

# Configure logging
log = structlog.get_logger()

# Intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Bot instance
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Placeholder imports for core modules (to be expanded)
from core import command_handler, event_dispatcher, guild_settings

@bot.event
async def on_ready():
    log.info("Bot is online", user=str(bot.user))

# Startup
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        log.error("Failed to start bot", error=str(e))
