import os as _os
import discord as _discord




# } file body end

bot = _discord.Bot(intents=_discord.Intents.all())


def run_bot():
	bot.run(_os.getenv('DISCORD_BOT_TOKEN'))

# file body begin {


# other begin {

__all__ = [n for n in globals() if n[:1] != '_']

# } other end
